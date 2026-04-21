from fastapi import FastAPI
from models import UsuarioDB, RepuestoDB
from database import engine, Base
from routes.repuestos import router as repuestos_router


app = FastAPI()
Base.metada.create_all(bind=engine)
app.include_router(repuestos_router)


