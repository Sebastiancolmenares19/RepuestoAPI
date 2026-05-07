from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict


class UsuarioCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: str
    email: str
    password: str = Field(..., alias='hashed_password')

    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if len(value.encode('utf-8')) > 72:
            raise ValueError('La contraseña no puede superar 72 bytes')
        return value

class UsuarioResponse(BaseModel):
    username: str
    email: str

    class Config: 
        from_attributes = True

class UsuarioUpdate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = Field(None, alias='hashed_password')

    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if value is None:
            return value
        if len(value.encode('utf-8')) > 72:
            raise ValueError('La contraseña no puede superar 72 bytes')
        return value

class RepuestoCreate(BaseModel):
    marca: str
    modelo: str
    precio: int
    stock: int
    categoria_id: int

class RepuestoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    marca: str
    modelo: str
    precio: int
    stock: int
    categoria_id: int

class RepuestoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    precio: Optional[int] = None
    stock: Optional[int] = None
    categoria_id: Optional[int] = None

class CategoriaCreate(BaseModel):
    nombre: str

class CategoriaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str

class CategoriaWithRepuestosResponse(CategoriaResponse):
    repuestos: list[RepuestoResponse] = []

class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = None