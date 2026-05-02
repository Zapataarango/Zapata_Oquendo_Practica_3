from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import relationship
from app.db import Base

class Laboratorio(Base):
    __tablename__ = "laboratorios"
    __table_args__ = {"schema": "jwt_grupo_2"}

    id_laboratorio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(255), nullable=False)
    activo = Column(Boolean, nullable=False, server_default=text("true"))

    tickets = relationship("Ticket", back_populates="laboratorio")