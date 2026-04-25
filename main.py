from fastapi import FastAPI
from fastapi.responses import JSONResponse
from exceptions import AlreadyExist, NotFound
from database import engine, Base
from routes.repuestos import router as repuestos_router
from routes.usuarios import router as usuarios_router
from routes.categorias import router as categorias_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(repuestos_router)
app.include_router(usuarios_router)
app.include_router(categorias_router)

@app.exception_handler(AlreadyExist)
async def user_already_exist_handler(request, exc):
    return JSONResponse(
        status_code= 409,
        content={"detail": "Recurso ya existe"}
    )

@app.exception_handler(NotFound)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code= 404,
        content={"detail": "Recurso no encontrado"}
        )



