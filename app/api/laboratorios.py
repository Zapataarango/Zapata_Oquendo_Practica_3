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
    return crud.obtener_laboratorios(db)

@router.get("/{id_laboratorio}", response_model=schemas.LaboratorioOut, dependencies=[Depends(require_scopes("laboratorios:read"))])
def obtener_laboratorio(id_laboratorio: int, db: Session = Depends(get_db)):
    lab = crud.obtener_laboratorio_por_id(db, id_laboratorio)
    if not lab:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return lab

@router.delete("/{id_laboratorio}", status_code=204)
def borrar_laboratorio(
    id_laboratorio: int, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("laboratorios:delete"))
):
    exito = crud.eliminar_laboratorio(db, id_laboratorio)
    if not exito:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return None