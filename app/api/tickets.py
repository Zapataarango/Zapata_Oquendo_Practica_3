from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app import crud, schemas
from app.security.auth import require_scopes

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)

@router.post("/", response_model=schemas.TicketOut, dependencies=[Depends(require_scopes("tickets:create"))])
def crear_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.crear_ticket(db, ticket)

@router.get("/", response_model=List[schemas.TicketOut], dependencies=[Depends(require_scopes("tickets:read"))])
def listar_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db)

@router.get("/{id_ticket}", response_model=schemas.TicketOut, dependencies=[Depends(require_scopes("tickets:read"))])
def obtener_ticket(id_ticket: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket_by_id(db, id_ticket)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    return ticket

@router.patch("/{id_ticket}/estado", response_model=schemas.TicketOut, dependencies=[Depends(require_scopes("tickets:update"))])
def actualizar_estado_ticket(id_ticket: int, data: schemas.TicketUpdateEstado, db: Session = Depends(get_db)):
    ticket_actualizado = crud.actualizar_estado_ticket(db, id_ticket, data.estado)
    if not ticket_actualizado:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    return ticket_actualizado