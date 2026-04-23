from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria,CategoriaDB


router = APIRouter(
    prefix = "/categoria",
    tags = ["categoria"]
)

@router.post("/")
def crear_categoria(categoria: CategoriaDB, db: Session = Depends(get_db)):

    nueva_categoria = CategoriaDB(nombre=categoria.nombre)

    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)

    return{"mensaje" : "Categoria creada"}

@router.get("/")
def obtener_categorias(db: Session = Depends(get_db)):

    categorias = db.query(CategoriaDB).all()

    return[
        {
            "id" : c.id,
            "nombre": c.nombre
        }
        for c in categorias
    ]

@router.get("/{categoria_id}/repuestos")
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(CategoriaDB)\
    .filter(CategoriaDB.id == categoria_id)\
    .first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail=f"Categoria no encontrada"
        )
    
    return {
        "id": categoria.id,
        "nombre": categoria.nombre
    }