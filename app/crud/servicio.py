from sqlalchemy.orm import Session
from app.models import Servicio
from app.schemas.servicio import ServicioCreate

def get_servicios(db: Session):
    return db.query(Servicio).filter(Servicio.activo == True).all()

def crear_servicio(db: Session, servicio: ServicioCreate):
    db_servicio = Servicio(**servicio.model_dump())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio