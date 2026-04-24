from exceptions import AlreadyExist, NotFound
from models import CategoriaDB

def get_by_nombre(db, categoria: str):
    return db.query(CategoriaDB)\
    .filter(CategoriaDB.nombre == categoria)\
    .first()

def get_by_id(db, categoria_id: int):
    return db.query(CategoriaDB)\
    .filter(CategoriaDB.id == categoria_id)\
    .first()

def get_categorias(db):
    return db.query(CategoriaDB). all()

def get_categoria(db, categoria_id):
    categoria = get_by_id(db, categoria_id)

    if not categoria:
        raise NotFound()
    return categoria

def create(db, categoria):
    nueva = CategoriaDB(nombre = categoria.nombre)

    db.add(nueva)
    return nueva

def delete(db, categoria):
    db.delete(categoria)
