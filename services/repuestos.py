from crud.repuestos import delete, get_by_id, create  
from crud.repuestos import get_repuestos as get_repuestos_crud
from crud.repuestos import get_repuesto as get_repuesto_crud
from exceptions import AlreadyExist, NotFound

def create_repuesto(db, repuesto_data): 
    nuevo_repuesto = create(db, repuesto_data)

    db.commit()
    db.refresh(nuevo_repuesto)
    return nuevo_repuesto

def get_repuestos(db):
    return get_repuestos_crud(db)

def get_repuesto(db, repuesto_id):
    return get_repuesto_crud(db, repuesto_id)

def update_repuesto(db, repuesto_id, repuesto_update):
    # Buscamos el repuesto por su ID real
    repuesto = get_by_id(db, repuesto_id)

    if not repuesto:
        raise NotFound()
    
    data = repuesto_update.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(repuesto, key, value)

    db.commit()
    db.refresh(repuesto)
    return repuesto

def delete_repuesto(db, repuesto_id):
    repuesto = get_by_id(db, repuesto_id)

    if not repuesto:
        raise NotFound()
    
    delete(db, repuesto)
    db.commit()
    return {"message": "Repuesto eliminado correctamente"}