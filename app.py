import os
import base64
from flask import Flask, Response, request, jsonify, send_from_directory, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_restful import Api
from resources.routes import initialize_routes
from PIL import Image, ImageOps

from models.job import Jobs, LogError
from models.db import Session , engine,connection_db
import redis
from rq import Queue, get_current_job
from datetime import datetime

# Import the time module to include some time delay in the application
import time

app = Flask(__name__)

# Make a connection of the queue and redis
r = redis.Redis()
q = Queue(connection=r)

session = Session()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12346@localhost:5432/test"
api = Api(app)
db = SQLAlchemy(app)

initialize_routes(api)

process = ['Invertir los colores', 'Pasar a Blanco y Negro', 'Rotar la imagen 180 grados', 'Invertir la sobre el eje vertical'] 
path=os.path.abspath(os.curdir+'/static/input/')
path2=os.path.abspath(os.curdir+'/static/output/') 

def insertLog(text):
    new_log = LogError(description=text)
    session.add(new_log)
    session.commit()

def task_in_imge(t): 
    
    delay = 5 
 
    time.sleep(delay)

    name = time.time()
    name = int(name)
    pick_name = str(name)+'.png'
 
    im_b64_inicial = t.split(sep=',')
        
    with open(path+"/"+pick_name, "wb") as fh:
            
        fh.write(base64.urlsafe_b64decode(im_b64_inicial[1]))

    image_file = Image.open(path+"/"+pick_name) # abrir imagen

    image_file2 = image_file.convert('1') # convertir imagen a blanco y negro
    image_file2.save(path2+'/wb'+pick_name)

    updateStatusJob(get_current_job().id, process[1])

    image_file3 = image_file.rotate(180) # rotar imagen
    image_file3.save(path2+'/rotar_'+pick_name)

    updateStatusJob(get_current_job().id, process[2])

    im = image_file.convert('L') # invertir colores
    im = ImageOps.invert(im)
    im.save(path2+'/inv'+pick_name)

    updateStatusJob(get_current_job().id, process[0])
    
    flip_img = image_file.transpose(Image.FLIP_TOP_BOTTOM) # voltear vertical
    flip_img.save(path2+'/vol_'+pick_name)
    
    updateStatusJob(get_current_job().id, process[3])
 
    print(get_current_job().id)
 
    return len(t)

@app.route('/')
def hello():

    return 'hellow-word'

@app.route('/get-job')
def getJob():
    
    try:
        if request.form['job_id']:
            works = session.query(Jobs).filter(Jobs.job_id == request.form['job_id'])
            results = {}
            for work in works:
                result = {}
                result['name_job'] = work.name_job
                result['estatus'] = work.estatus
                result['start_time'] = work.start_time
                result['end_time'] = work.end_time
                result['job_id'] = work.job_id

                results[work.id] = result

            menssage = "get job se ejecuto correctamente"
            insertLog(menssage)
            return results
        else:
                request.close()
                return {'error':'Faltan datos por ingresar'}, 401
    except:
            request.close()
            return {'error':'Faltan datos por ingresar'},401

@app.route('/get-log')
def getLog():
    try:
        
        logs = session.query(LogError).filter(LogError.date >= request.form['fecha-desde'], LogError.date <= request.form['fecha-hasta'])
        results = {}
        for log in logs:
            result = {}
            result['description'] = log.description
            result['date'] = log.date
            results[log.id] = result

        menssage = "get log se ejecuto correctamente"
        insertLog(menssage)
        
        return results
    except:
            request.close()
            return {'error':'Faltan datos por ingresar'},401

@app.route("/api/store", methods=["POST"])
def store():
    
    if request.form['image']: 
 
        job= q.enqueue(task_in_imge, request.form['image'])
 
        q_len = len(q)
        insertJob(job.id)

        final = "Turno es: "+ str(q_len) +" Tu id: "+job.id
 
        return final

    return "No se encontro imagen"  

def insertJob(id_j):
    for prs in process:
        now = datetime.now()
        new_jobs = Jobs(name_job=prs, estatus='process', end_time='2022-01-01',job_id=id_j)
        session.add(new_jobs)
        session.commit()

def updateStatusJob(id_job, name_job):
    now = datetime.now()
    j = session.query(Jobs).filter(Jobs.job_id == id_job, Jobs.name_job == name_job )
    for i in j:
        i.estatus = 'success'
        i.end_time = now
        session.commit()
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)