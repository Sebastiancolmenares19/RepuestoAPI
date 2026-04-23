from crud.usuarios import create, delete, get_by_username, refresh, save
from crud.usuarios import get_usuarios as get_usuarios_crud
from crud.usuarios import get_usuario as get_usuario_crud
from exceptions import AlreadyExist, NotFound


def create_usuario(db, user):

    usuario_existente= get_by_username(db, user.username)

    if usuario_existente:
        raise AlreadyExist()
    
    return create(db, user)


def get_usuarios(db):
    return get_usuarios_crud(db)

def get_usuario(db):
    return get_usuario_crud(db)


def update_usuario(db, usuario_id, user):

    usuario = get_by_username(db,usuario_id, user)

    if not usuario:
        raise NotFound()
    
    data = user.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(usuario, key, value)

    save(db)
    return refresh(db, usuario)

def delete_usuario(db, username):

    usuario = get_by_username(db, username)

    if not usuario:
        raise NotFound()
    
    delete(db,usuario)
    
    return {"message": "Usuario eliminado"}