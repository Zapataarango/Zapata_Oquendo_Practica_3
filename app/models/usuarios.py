from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import relationship
from app.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "jwt_grupo_2"}

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False, server_default=text("true"))

    tickets_solicitados = relationship("Ticket", foreign_keys="[Ticket.id_solicitante]", back_populates="solicitante")
    tickets_gestionados = relationship("Ticket", foreign_keys="[Ticket.id_responsable]", back_populates="responsable")
    tickets_asignados = relationship("Ticket", foreign_keys="[Ticket.id_asignado]", back_populates="tecnico_asignado")