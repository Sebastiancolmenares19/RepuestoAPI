from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import verify_password, create_access_token, get_current_user   
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

@router.get("/me", response_model=UsuarioResponse)
def read_current_user(current_username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.username == current_username).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/{usuario_id}", response_model= UsuarioResponse)
def obtener_usuario(usuario_id: int, db:Session = Depends(get_db)):
    return get_usuario(db, usuario_id) 

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, user: UsuarioUpdate, db: Session = Depends(get_db)):   
    return update_usuario(db, usuario_id, user)

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return delete_usuario(db, usuario_id)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.username == form_data.username).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no existe")
    
    if not verify_password(form_data.password, usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    token = create_access_token(data={"sub": usuario.username})
    
    return {"access_token": token, "token_type": "bearer"}