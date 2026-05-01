from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import relationship
from app.db import Base

class Servicio(Base):
    __tablename__ = "servicios"
    __table_args__ = {"schema": "Laboratorios"}

    id_servicio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, server_default=text("true"))

    tickets = relationship("Ticket", back_populates="servicio")