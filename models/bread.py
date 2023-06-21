from config.database import base
from sqlalchemy import Column, Integer, Float, String

class Bread(base):
    __tablename__ = "pan"

    id = Column(Integer, primary_key=True)
    producto = Column(String)
    precio = Column(Float)
    tipo = Column(String)
