from config.database import base
from sqlalchemy import Column, String, Integer

class User(base):    
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True)
    usuario= Column(String)
    password= Column(String)