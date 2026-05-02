from sqlalchemy.orm import Session
from app.models import Servicio
from app.schemas.servicio import ServicioCreate

def obtener_servicios(db: Session):
    return db.query(Servicio).filter(Servicio.activo == True).all()

def obtener_servicio_por_id(db: Session, servicio_id: int):
    return db.query(Servicio).filter(Servicio.id_servicio == servicio_id, Servicio.activo == True).first()

def crear_servicio(db: Session, servicio: ServicioCreate):
    db_servicio = Servicio(**servicio.model_dump())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def eliminar_servicio(db: Session, ticket_id: int):
    db_ticket = db.query(Servicio).filter(Servicio.id_ticket == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
        return True
    return False