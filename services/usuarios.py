from crud.usuarios import create, delete, get_by_username, refresh, save, get_by_id
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

def get_usuario(db, usuario_id):
    return get_usuario_crud(db, usuario_id)


def update_usuario(db, usuario_id, user):

    usuario = get_by_id(db,usuario_id)

    if not usuario:
        raise NotFound()
    
    if user.username:
        existing = get_by_username(db, user.username)
        if existing and existing.id != usuario_id:
            raise AlreadyExist
    
    data = user.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(usuario, key, value)

    save(db)
    return refresh(db, usuario)

def delete_usuario(db, usuario_id):

    usuario = get_by_id(db, usuario_id)

    if not usuario:
        raise NotFound()
    
    delete(db,usuario)
    
    return {"message": "Usuario eliminado"}