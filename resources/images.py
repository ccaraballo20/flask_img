# import time
import os
# import uuid
# import gc
# import cv2
import base64
# import json  
# import requests  
# from flask import Response, request, jsonify, send_from_directory, make_response, render_template
from flask_restful import Resource
# from werkzeug.utils import secure_filename
from models.job import Jobs
from models.db import Session , engine, connection_db
from models.db import Base, engine

session = Session()

# work_dir=os.path.abspath(os.curdir+'/')

class getServicios(Resource):
    def get(self):
        return 'hola desde los servicios'

class getHolaEye(Resource):
    def get(self):
        return "Welcome to eye"

class getJob(Resource):
    def get(self):
        with engine.connect() as con:
            nueva_img = Images(id=4,nombre_img="{aaa}", estatus=0)
            session.add(nueva_img)
            session.commit()
            imgs = Images.query.all()
        # imgs = session.query(Images).all()
        # results = [
        #     {
        #         "id": imgs.id,
        #         "nombre_img": imgs.nombre_img,
        #         "estatus": imgs.estatus
        #     } for car in cars]

        return "results"

class getLog(Resource):
    def get(self):
        return "get log"