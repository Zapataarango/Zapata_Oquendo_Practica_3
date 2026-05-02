from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app import crud, schemas
from app.security.auth import require_scopes

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"],
)

@router.post("/", response_model=schemas.ServicioOut, dependencies=[Depends(require_scopes("servicios:create"))])
def crear_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(get_db)):
    return crud.crear_servicio(db, servicio)

@router.get("/", response_model=List[schemas.ServicioOut], dependencies=[Depends(require_scopes("servicios:read"))])
def listar_servicios(db: Session = Depends(get_db)):
    return crud.obtener_servicios(db)

@router.get("/{id_servicio}", response_model=schemas.ServicioOut, dependencies=[Depends(require_scopes("servicios:read"))])
def obtener_servicio(id_servicio: int, db: Session = Depends(get_db)):
    srv = crud.obtener_servicio_por_id(db, id_servicio)
    if not srv:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return srv

@router.delete("/{id_servicio}", status_code=204)
def borrar_servicio(
    id_servicio: int, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("servicios:delete"))
):
    exito = crud.eliminar_servicio(db, id_servicio)
    if not exito:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return None