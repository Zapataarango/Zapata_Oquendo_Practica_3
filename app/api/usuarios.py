from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app import crud, schemas
from app.security.auth import require_scopes

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)

@router.post("/", response_model=schemas.UsuarioOut, dependencies=[Depends(require_scopes("usuarios:create"))])
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@router.get("/", response_model=List[schemas.UsuarioOut], dependencies=[Depends(require_scopes("usuarios:read"))])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)

@router.get("/{id_usuario}", response_model=schemas.UsuarioOut, dependencies=[Depends(require_scopes("usuarios:read"))])
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario_by_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario