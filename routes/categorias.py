from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import CategoriaCreate, CategoriaResponse, RepuestoResponse
from services.categoria import create_categoria, get_categoria, get_categorias, get_repuestos_por_categoria


router = APIRouter(
    prefix = "/categoria",
    tags = ["categoria"]
)

@router.post("/", response_model= CategoriaResponse)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return create_categoria(db, categoria)

@router.get("/", response_model=list[CategoriaResponse])
def obtener_categorias(db: Session = Depends(get_db)):
    return get_categorias(db)

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return get_categoria(db, categoria_id)

@router.get("/{categoria_id}/repuestos", response_model=list[RepuestoResponse])
def obtener_repuestos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return get_repuestos_por_categoria(db, categoria_id)