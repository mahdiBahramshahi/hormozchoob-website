from itertools import count
from app import db
from sqlalchemy import Column , Integer , String , DateTime
import datetime as dt


class File(db.Model):
    id = Column(Integer, primary_key = True)
    project_name= Column(String(64), nullable=False , unique=False)
    height = Column(String(18), nullable=False , unique=False)
    width = Column(String(18), nullable=False , unique=False)
    qty = Column(String(18), nullable=False , unique=False)
    pvc = Column(String(64), nullable=True , unique=False)
    username = Column(String(128) ,nullable=False , unique=False )
    filename =  Column(String(256) , nullable=True , unique=True)
    upload_date =  Column(DateTime(), nullable=False , unique=False , default=dt.datetime.utcnow)

