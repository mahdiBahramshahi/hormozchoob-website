from app import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__='users'
    id = Column(Integer(),primary_key=True)
    email = Column(String(128),nullable=False,unique=True)
    password = Column(String(128),nullable=False,unique=False)
    role = Column(Integer(),nullable=False,default=0)
    username = Column(String(128),nullable=False,unique=True)
    phone_number = Column(String(18) , nullable=False , unique=False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password ,password)

    def is_admin(self):
        return self.role == 1