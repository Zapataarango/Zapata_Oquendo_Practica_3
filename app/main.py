from fastapi import FastAPI
from app.api.laboratorios import router as router_laboratorios
 
 
app = FastAPI(
    title="Gestión universitaria",
    version="0.1",
    description="API desarrollada para el curso de Aplicaciones y servicios"
)
 
app.include_router(router_laboratorios)
 
@app.get("/")
def root():
    return {"Message": "Status OK"}