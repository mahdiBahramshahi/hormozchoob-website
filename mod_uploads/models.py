from enum import unique
from itertools import count

from sqlalchemy.sql.expression import null, true
from wtforms.widgets.html5 import ColorInput
from app import db
from sqlalchemy import Column , Integer , String , DateTime
import datetime as dt


class File(db.Model):
    id = Column(Integer, primary_key = True)
    project_name= Column(String(32), nullable=False , unique=False)
    username = Column(String(32) ,nullable=False , unique=False )
    height = Column(String(10), nullable=False , unique=False)
    width = Column(String(10), nullable=False , unique=False)
    qty = Column(String(10), nullable=False , unique=False)
    pvc = Column(String(64), nullable=True , unique=False)
    mdf_model = Column(String(128) , nullable=False , unique=False)
    Charkhesh = Column(String(64) , nullable=False , unique=False)
    shiar = Column(String(64) , nullable=False , unique=False)
    farsi = Column(String(64) , nullable=False , unique=False)
    about = Column(String(1028) , nullable=True , unique=False)
    filename =  Column(String(256) , nullable=True , unique=True)
    upload_date =  Column(DateTime(), nullable=False , unique=False , default=dt.datetime.utcnow)



class kh_project(db.Model):
    __tablename__= 'kh_projects'
    id = Column(Integer, primary_key = True)
    project_name = Column(String(128), nullable=False , unique=True)
    username = Column(String(128) ,nullable=False , unique=False )
    slug = Column(String(256) , nullable=False, unique=True)
    date =  Column(DateTime(), nullable=False , unique=False , default=dt.datetime.utcnow)
