from database import Base
from sqlalchemy import Column, Integer, String , Float 
from pydantic import BaseModel  

class Usuario(BaseModel):
    id: int
    username: str
    email: set
    hashed_password: str

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key= True, index = True )
    username = Column(String, unique = True)
    email = Column(String)
    hashed_password = Column(String)

class Repuesto(BaseModel):
    id: int
    marca: str
    modelo: str
    precio: float
    stock: int

class RepuestoDB(Base):
    __tablename__ = "repuesto"

    id = Column(Integer, primary_key= True, index = True )
    marca = Column(String)
    modelo = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
