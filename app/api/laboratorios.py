from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app import crud, schemas
from app.security.auth import require_scopes

router = APIRouter(
    prefix="/laboratorios",
    tags=["Laboratorios"],
)

@router.post("/", response_model=schemas.LaboratorioOut, dependencies=[Depends(require_scopes("laboratorios:create"))])
def crear_laboratorio(laboratorio: schemas.LaboratorioCreate, db: Session = Depends(get_db)):
    return crud.crear_laboratorio(db, laboratorio)

@router.get("/", response_model=List[schemas.LaboratorioOut], dependencies=[Depends(require_scopes("laboratorios:read"))])
def listar_laboratorios(db: Session = Depends(get_db)):
    return crud.get_laboratorios(db)

@router.get("/{id_laboratorio}", response_model=schemas.LaboratorioOut, dependencies=[Depends(require_scopes("laboratorios:read"))])
def obtener_laboratorio(id_laboratorio: int, db: Session = Depends(get_db)):
    lab = crud.get_laboratorio_by_id(db, id_laboratorio)
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return lab