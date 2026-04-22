from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario,UsuarioDB

router = APIRouter(
    prefix = "/usuarios",
    tags = ["usuarios"]
)

@router.post("/")
def crear_usuario(usuario: Usuario, db: Session = Depends(get_db)):

    usuario_existente = db.query(UsuarioDB)\
    .filter(UsuarioDB.username == usuario.username)\
    .first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="El usuario ya existe"
    )

    nuevo_usuario = UsuarioDB(
        username = usuario.username,
        email = usuario.email,
        hashed_password = usuario.hashed_password
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {
        "mensaje" : "Usuario creado"
    }

@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).all()

    return [
        {
            "id": s.id,
            "username": s.username,
            "email": s.email,
            "hashed_password": s.hashed_password
        }

        for s in usuario
    ]

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, db:Session = Depends(get_db)):
    usuario = db.query(UsuarioDB)\
    .filter(UsuarioDB.id == usuario_id)\
    .first()

    if not usuario:
        raise HTTPException(
            status_code= 404,
            detail =f"Usuario no encontrado"
        )
    
    return {
        "id": usuario.id,
        "username": usuario.username,
        "email": usuario.email,
        "hashed_password": usuario.hashed_password
    }

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, data: Usuario, db: Session = Depends(get_db)):
    
    usuario = db.query(UsuarioDB)\
    .filter(UsuarioDB.id == usuario_id)\
    .first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail=f"Repuesto con id {usuario_id} no encontrado"
        )
    
    #actualizar campos
    usuario.username = data.username
    usuario.email = data.email
    usuario.hashed_password = data.hashed_password

    db.commit()
    db.refresh(usuario)

    return {
        "mensaje" : "Usuario actualizado"
    }

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):

    usuario = db.query(UsuarioDB)\
    .filter(UsuarioDB.id == usuario_id)\
    .first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con id {usuario_id} no encontrado"
        )
    
    db.delete(usuario)
    db.commit()

    return{
        "mensaje" : "Usuario eliminado"
    }
