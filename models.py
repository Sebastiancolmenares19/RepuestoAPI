from database import Base
from sqlalchemy import Column, Integer, String , Float, ForeignKey
from sqlalchemy.orm import relationship

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key= True, index = True )
    username = Column(String, unique = True)
    email = Column(String)
    hashed_password = Column(String)

class RepuestoDB(Base):
    __tablename__ = "repuesto"

    id = Column(Integer, primary_key= True, index = True )
    marca = Column(String)
    modelo = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("CategoriaDB", back_populates="repuestos")


class CategoriaDB(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key= True, index= True)
    nombre = Column(String, unique=True)

    repuestos = relationship("RepuestoDB", back_populates="categoria")
