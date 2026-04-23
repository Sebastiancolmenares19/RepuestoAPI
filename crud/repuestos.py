from exceptions import NotFound
from models import RepuestoDB


def get_by_id(db, repuesto_id):
    return db.query(RepuestoDB)\
    .filter(RepuestoDB.id == repuesto_id)\
    .first()

def get_repuestos(db):
    return db.query(RepuestoDB).all()

def get_repuesto(db, repuesto_id):
    
    repuesto = get_by_id(db, repuesto_id)

    if not repuesto:
        raise NotFound()
    return repuesto


def create(db, repuesto):

    nuevo_repuesto = RepuestoDB(
        **repuesto.model_dump(exclude={"id"})
    )

    db.add(nuevo_repuesto)
    db.commit()
    db.refresh(nuevo_repuesto)

    return nuevo_repuesto

def save(db):
    db.commit()

def refresh(db,obj):
    db.refresh(obj)
    return obj

def delete(db, repuesto):
    db.delete(repuesto)
    db.commit()