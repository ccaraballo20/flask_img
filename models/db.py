from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from config import connection_db

# Local host
connection_db = "postgresql://postgres:123456@localhost:5432/test"
Base = declarative_base()

engine = create_engine(connection_db)

Session = sessionmaker(bind=engine)