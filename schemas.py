from typing import Optional
from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    username: str
    email: str
    hashed_password: str

class UsuarioResponse(BaseModel):
    username: str
    email: str

    class Config: 
        from_attributes = True

class UsuarioUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None

class RepuestoCreate(BaseModel):
    marca: str
    modelo: str
    precio: int
    stock: int

class RepuestoResponse(BaseModel):
    marca: str
    modelo: str
    precio: int
    stock: int

    class Config: 
        from_attributes = True

class RepuestoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    precio: Optional[int] = None
    stock: Optional[int] = None

class CategoriaCreate(BaseModel):
    nombre: str

class CategoriaResponse(BaseModel):
    nombre: str
    
    class Config: 
        from_attributes = True

class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = None