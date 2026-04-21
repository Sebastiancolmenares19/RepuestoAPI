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
        nombre = repuesto.nombre,
        marca = repuesto.marca,
        precio = repuesto.precio,
        stock = repuesto.stock
    )

    db.add(nuevo_repuesto)
    db.commit()
    db.refresh(nuevo_repuesto)

    return {
        "mensaje": "Repuesto creado"
    }

    