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

@router.post("/", response_model=schemas.TicketOut)
def crear_ticket(
    ticket: schemas.TicketCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:crear"))
):
    return crud.crear_ticket(db, ticket, id_solicitante=current_user.id_usuario)

@router.get("/", response_model=List[schemas.TicketOut])
def listar_tickets(
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:ver_propios"))
):
    if "tickets:ver_todos" in current_user.scopes:
        return crud.obtener_todos_los_tickets(db)
    
    return crud.obtener_tickets_propios(db, usuario_id=current_user.id_usuario)

@router.get("/{id_ticket}", response_model=schemas.TicketOut)
def obtener_ticket(
    id_ticket: int, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:ver_propios"))
):
    ticket = crud.obtener_ticket_por_id(db, id_ticket)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    
    if "tickets:ver_todos" not in current_user.scopes:
        if ticket.id_solicitante != current_user.id_usuario and ticket.id_asignado != current_user.id_usuario:
            raise HTTPException(status_code=403, detail="No tiene permiso para ver este ticket")
            
    return ticket

@router.patch("/{id_ticket}/estado", response_model=schemas.TicketOut)
def cambiar_estado_ticket(
    id_ticket: int, 
    data: schemas.TicketUpdateEstado, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:ver_propios"))
):
    return crud.cambiar_estado_ticket(
        db=db, 
        id_ticket=id_ticket, 
        nuevo_estado=data.nuevo_estado, 
        usuario_actual=current_user
    )

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app import crud, schemas
from app.security.auth import require_scopes

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.patch("/{id_ticket}/asignar", response_model=schemas.TicketOut)
def asignar_ticket(
    id_ticket: int, 
    data: schemas.TicketAsignar, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:ver_propios"))

):
    return crud.asignar_ticket_tecnico(
        db=db, 
        id_ticket=id_ticket, 
        id_asignado=data.id_asignado,
        usuario_que_asigna=current_user 
    )

@router.delete("/{id_ticket}", status_code=204)
def eliminar_ticket(
    id_ticket: int, 
    db: Session = Depends(get_db),
    current_user = Depends(require_scopes("tickets:ver_propios"))
):
    crud.eliminar_ticket(db, id_ticket, usuario_actual=current_user)
    return None

@router.get("/", response_model=List[schemas.TicketOut], dependencies=[Depends(require_scopes("tickets:ver_todos"))])
def listar_tickets(db: Session = Depends(get_db)):
    return crud.obtener_todos_los_tickets(db)

@router.post("/", response_model=schemas.TicketOut, dependencies=[Depends(require_scopes("tickets:crear"))])
def crear_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, ticket)