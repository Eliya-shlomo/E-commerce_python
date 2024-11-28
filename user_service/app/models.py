from sqlalchemy import Colomn,String,Integer
from .db import Base

class User(Base):
    __tabalename__ = "users"

    id = Colomn(Integer,Primery_key=True,index=True)
    username = Colomn(String,unique=True,index=True,nullable=False)
    email = Colomn(String,unique=True,index=true,nullable=False)
    hashed_password = Colomn(String,nullable = False)
    
