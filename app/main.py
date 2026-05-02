from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.usuarios import router as usuarios_router
from app.api.laboratorios import router as laboratorios_router
from app.api.servicios import router as servicios_router
from app.api.tickets import router as tickets_router
from app.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestión de Laboratorios",
    description="API para el control de soportes técnicos y laboratorios",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(laboratorios_router)
app.include_router(servicios_router)
app.include_router(tickets_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Gestión de Laboratorios", "status": "running"}