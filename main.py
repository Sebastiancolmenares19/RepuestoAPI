from fastapi import FastAPI
from models import UsuarioDB, RepuestoDB
from database import engine, Base
from routes.repuestos import router as repuestos_router
from routes.usuarios import router as usuarios_router


app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(repuestos_router)
app.include_router(usuarios_router)


