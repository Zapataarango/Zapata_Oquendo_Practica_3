from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.models import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdateEstado

def crear_ticket(db: Session, ticket: TicketCreate, id_solicitante: int):
    db_ticket = Ticket(
        **ticket.model_dump(),
        id_solicitante=id_solicitante,
        estado="solicitado"
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session):
    return db.query(Ticket).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id_ticket == ticket_id).first()

def actualizar_estado_ticket(db: Session, ticket_id: int, update_data: TicketUpdateEstado):
    db_ticket = get_ticket_by_id(db, ticket_id)
    if db_ticket:
        db_ticket.estado = update_data.estado
        if update_data.estado == "finalizado":
            db_ticket.fecha_finalizacion = datetime.now(timezone.utc)
        
        db.commit()
        db.refresh(db_ticket)
    return db_ticket