from exceptions import NotFound
from models import UsuarioDB

def get_by_username(db, username: str):
    return db.query(UsuarioDB)\
    .filter(UsuarioDB.username == username)\
    .first()

def get_by_id(db, usuario_id: int):
    return db.query(UsuarioDB)\
    .filter(UsuarioDB.id == usuario_id)\
    .first()

def get_usuarios(db):
    return db.query(UsuarioDB).all()

def get_usuario(db, usuario_id):
    usuario = get_by_id(db, usuario_id)

    if not usuario:
        raise NotFound()
    return usuario

def create(db, usuario):
    nuevo_usuario = UsuarioDB(
        username = usuario.username,
        email = usuario.email,
        hashed_password = usuario.hashed_password
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

def save(db):
    db.commit()

def refresh(db,obj):
    db.refresh(obj)
    return obj

def delete(db, usuario):
    db.delete(usuario)
    db.commit()