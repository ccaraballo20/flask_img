import datetime
from sqlalchemy import Column,String , Integer, Date, DateTime
from .db import Base,engine
# from sqlalchemy.schema import ForeignKey
# from sqlalchemy.orm import relationship
# from app import db

class Jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer,autoincrement=True , primary_key=True)
    name_job = Column(String(200))
    estatus = Column(String(200))
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(Date)
    job_id = Column(String(200))


    def __init__(self, name_job, estatus, end_time, job_id):
        self.name_job = name_job
        self.estatus = estatus
        self.end_time = end_time
        self.job_id = job_id

class LogError(Base):
    __tablename__ = 'log_error'
    id = Column(Integer,autoincrement=True, primary_key=True)
    description = Column(String(200))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, description):
        self.description = description
    
Base.metadata.create_all(engine)