from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Repuesto, RepuestoDB

router = APIRouter(
    prefix="/repuestos",
    tags=["repuestos"]
)

@router.post("/")
def crear_repuesto(repuesto: Repuesto, db: Session = Depends(get_db)):
    nuevo_repuesto = RepuestoDB(
        marca = repuesto.marca,
        modelo = repuesto.modelo,
        precio = repuesto.precio,
        stock = repuesto.stock
    )

    db.add(nuevo_repuesto)
    db.commit()
    db.refresh(nuevo_repuesto)

    return {
        "mensaje": "Repuesto creado"
    }

@router.get("/")
def obtener_respuestos(db:Session = Depends(get_db)):
    repuestos = db.query(RepuestoDB).all()

    return [
        {
           "id": r.id,
            "marca": r.marca,
            "modelo": r.modelo,
            "precio": r.precio,
            "stock": r.stock 
        }

        for r in repuestos
    ]

@router.get("/{repuesto_id}")
def obtener_repuesto(repuesto_id: int, db: Session = Depends(get_db)):
    
    repuesto = db.query(RepuestoDB)\
    .filter(RepuestoDB.id == repuesto_id)\
    .first()

    if not repuesto:
        raise HTTPException(
            status_code=404,
            detail=f"Repuesto con id {repuesto_id} no encontrado"
        )
    
    return {
        "id": repuesto.id,
        "marca": repuesto.marca,
        "modelo": repuesto.modelo,
        "precio": repuesto.precio,
        "stock": repuesto.stock
    }

@router.put("/{repuesto_id}")
def actualizar_repuesto(repuesto_id: int, data: Repuesto, db: Session = Depends(get_db)):
    
    repuesto = db.query(RepuestoDB)\
    .filter(RepuestoDB.id == repuesto_id)\
    .first()

    if not repuesto:
        raise HTTPException(
            status_code=404,
            detail=f"Repuesto con id {repuesto_id} no encontrado"
        )
    
    #actualizar campos
    repuesto.nombre = data.nombre
    repuesto.marca = data.marca
    repuesto.precio = data.precio
    repuesto.stock = data.stock

    db.commit()
    db.refresh(repuesto)

    return {
        "mensaje" : "Repuesto actualizado"
    }

@router.delete("/{repuesto_id}")
def eliminar_repuesto(repuesto_id: int, db: Session = Depends(get_db)):

    repuesto = db.query(RepuestoDB)\
    .filter(RepuestoDB.id == repuesto_id)\
    .first()

    if not repuesto:
        raise HTTPException(
            status_code=404,
            detail=f"Repuesto con id {repuesto_id} no encontrado"
        )
    
    db.delete(repuesto)
    db.commit()

    return{
        "mensaje" : "Repuesto eliminado"
    }




    