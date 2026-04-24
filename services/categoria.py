from crud.categorias import  get_by_id, get_by_nombre, get_categorias as get_categorias_crud
from crud.categorias import get_categoria as get_categoria_crud
from crud.categorias import delete
from crud.categorias import create
from exceptions import AlreadyExist, NotFound


def create_categoria(db,categoria):

    if get_by_nombre(db, categoria.nombre):
        raise AlreadyExist()
    
    nuevo = create(db,categoria)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_categorias(db):
    return get_categorias_crud(db)

def get_categoria(db, categoria_id):
    return get_categoria_crud(db, categoria_id)

def update_categoria(db, categoria_id, categoria_update):

    categoria_obj = get_by_id(db, categoria_id)

    if not categoria_obj:
        raise NotFound()

    if categoria_update.nombre:
        existing = get_by_nombre(db, categoria_update.nombre)
        if existing and existing.id != categoria_id:
            raise AlreadyExist()

    data = categoria_update.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(categoria_obj, key, value)

    db.commit()
    db.refresh(categoria_obj)
    return categoria_obj

def delete_categoria(db, categoria_id):

    categoria = get_by_id(db, categoria_id)

    if not categoria:
        raise NotFound()
    
    delete(db, categoria)
    db.commit()

    return {"message": "Categoria eliminada"}