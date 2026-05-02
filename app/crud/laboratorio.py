from sqlalchemy.orm import Session
from app.models import Laboratorio
from app.schemas.laboratorio import LaboratorioCreate

def get_laboratorios(db: Session):
    return db.query(Laboratorio).all()

def crear_laboratorio(db: Session, laboratorio: LaboratorioCreate):
    db_lab = Laboratorio(**laboratorio.dict())
    db.add(db_lab)
    db.commit()
    db.refresh(db_lab)
    return db_lab

def get_laboratorio_by_id(db: Session, id_laboratorio: int):
    return db.query(Laboratorio).filter(Laboratorio.id_laboratorio == id_laboratorio).first()