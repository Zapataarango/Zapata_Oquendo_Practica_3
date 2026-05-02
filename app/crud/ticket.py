from sqlalchemy.orm import Session
from app.models import Ticket, Usuario
from app.schemas import TicketCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import HTTPException, status

def crear_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(
        titulo=ticket.titulo,
        descripcion=ticket.descripcion,
        prioridad=ticket.prioridad,
        id_laboratorio=ticket.id_laboratorio,
        id_servicio=ticket.id_servicio,
        id_solicitante=ticket.id_solicitante,
        estado="solicitado"
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def obtener_tickets(db: Session):
    return db.query(Ticket).all()

def obtener_ticket_por_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id_ticket == ticket_id).first()

def obtener_tickets_propios (db: Session, usuario_id: int):
    return db.query(Ticket).filter(
        (Ticket.id_solicitante == usuario_id) | 
        (Ticket.id_asignado == usuario_id)
    ).all()

def cambiar_estado_ticket(db: Session, id_ticket: int, nuevo_estado: str, usuario_actual: any):
    db_ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    estado_actual = db_ticket.estado
    scopes = usuario_actual.scopes

    reglas = {
        ("solicitado", "recibido"): "tickets:recibir",
        ("recibido", "asignado"): "tickets:asignar",
        ("asignado", "en_proceso"): "tickets:atender",
        ("en_proceso", "en_revision"): "tickets:atender",
        ("en_revision", "terminado"): "tickets:finalizar",
    }

    transicion = (estado_actual, nuevo_estado)

    if transicion not in reglas:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Transición no permitida: de {estado_actual} a {nuevo_estado}"
        )

    scope_requerido = reglas[transicion]
    if scope_requerido not in scopes:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"No tienes el permiso '{scope_requerido}' para esta acción"
        )

    if nuevo_estado in ["en_proceso", "en_revision"] and "admin" not in usuario_actual.rol:
        if db_ticket.id_asignado != usuario_actual.id_usuario:
            raise HTTPException(
                status_code=403,
                detail="Solo el técnico asignado a este ticket puede cambiar su estado"
            )

    db_ticket.estado = nuevo_estado
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
 

def eliminar_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id_ticket == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
        return True
    return False

def asignar_ticket_tecnico(db: Session, id_ticket: int, id_asignado: int, usuario_que_asigna: any):
    if "tickets:asignar" not in usuario_que_asigna.scopes:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso (tickets:asignar) para realizar esta operación"
        )

    db_ticket = db.query(Ticket).filter(Ticket.id_ticket == id_ticket).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    if db_ticket.estado != "recibido":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Estado inválido: {db_ticket.estado}. Debe estar en 'recibido'."
        )

    tecnico = db.query(Usuario).filter(Usuario.id_usuario == id_asignado).first()
    if not tecnico:
        raise HTTPException(status_code=404, detail="El técnico a asignar no existe")
    
    if tecnico.rol not in ["auxiliar", "tecnico_especializado", "admin"]:
        raise HTTPException(
            status_code=400, 
            detail="El usuario asignado debe tener un rol técnico (auxiliar o especialista)"
        )

    db_ticket.id_asignado = id_asignado
    db_ticket.estado = "asignado"

    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def obtener_todos_los_tickets(db: Session):
    return db.query(Ticket).all()
