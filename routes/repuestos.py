from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from crud.repuestos import get_repuesto, get_repuestos
from database import get_db
from models import RepuestoDB
from schemas import RepuestoCreate, RepuestoResponse, RepuestoUpdate
from services.repuestos import create_repuesto, delete_repuesto, update_repuesto

router = APIRouter(
    prefix="/repuestos",
    tags=["repuestos"]
)

@router.post("/", response_model=RepuestoResponse)
def crear_repuesto(repuesto: RepuestoCreate, db: Session = Depends(get_db)):
    return create_repuesto(db, repuesto)

@router.get("/", response_model=list[RepuestoResponse])
def obtener_respuestos(db:Session = Depends(get_db)):
    return get_repuestos(db)

@router.get("/{repuesto_id}", response_model=RepuestoResponse)
def obtener_repuesto(repuesto_id: int, db: Session = Depends(get_db)):    
    return get_repuesto(db,repuesto_id)

@router.put("/{repuesto_id}", response_model = RepuestoResponse)
def actualizar_repuesto(repuesto_id: int, repuesto: RepuestoUpdate, db: Session = Depends(get_db)):   
    return update_repuesto(db, repuesto_id, repuesto)

@router.delete("/{repuesto_id}")
def eliminar_repuesto(repuesto_id: int, db: Session = Depends(get_db)):
    return delete_repuesto(db, repuesto_id)




    