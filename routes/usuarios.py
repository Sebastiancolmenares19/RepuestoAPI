from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import UsuarioDB
from schemas import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from services.usuarios import create_usuario, delete_usuario, get_usuarios, get_usuario, update_usuario

router = APIRouter(
    prefix = "/usuarios",
    tags = ["usuarios"]
)

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, usuario)

@router.get("/", response_model =list[UsuarioResponse])
def obtener_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.get("/{usuario_id}", response_model= UsuarioResponse)
def obtener_usuario(usuario_id: int, db:Session = Depends(get_db)):
    return get_usuario(db, usuario_id) 

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, user: UsuarioUpdate, db: Session = Depends(get_db)):   
    return update_usuario(db, usuario_id, user)

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return delete_usuario(db, usuario_id)
