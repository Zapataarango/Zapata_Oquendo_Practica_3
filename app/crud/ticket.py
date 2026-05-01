from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship
from app.db import Base

class Ticket(Base):
    __tablename__ = "tickets"
    __table_args__ = {"schema": "Laboratorios"}

    id_ticket = Column(Integer, primary_key=True, index=True)
    
    id_solicitante = Column(Integer, ForeignKey("Laboratorios.usuarios.id_usuario"), nullable=False)
    id_laboratorio = Column(Integer, ForeignKey("Laboratorios.laboratorios.id_laboratorio"), nullable=False)
    id_servicio = Column(Integer, ForeignKey("Laboratorios.servicios.id_servicio"), nullable=False)
    id_responsable = Column(Integer, ForeignKey("Laboratorios.usuarios.id_usuario"), nullable=True)
    id_asignado = Column(Integer, ForeignKey("Laboratorios.usuarios.id_usuario"), nullable=True)

    titulo = Column(String(150), nullable=False)
    descripcion = Column(String(500), nullable=False)
    estado = Column(String(50), nullable=False, server_default=text("'abierto'"))
    prioridad = Column(String(20), nullable=False)
    
    observacion_responsable = Column(String(500), nullable=True)
    observacion_tecnico = Column(String(500), nullable=True)

    fecha_creacion = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=text("CURRENT_TIMESTAMP"))
    fecha_finalizacion = Column(DateTime, nullable=True)

    solicitante = relationship("Usuario", foreign_keys=[id_solicitante], back_populates="tickets_solicitados")
    laboratorio = relationship("Laboratorio", back_populates="tickets")
    servicio = relationship("Servicio", back_populates="tickets")
    responsable = relationship("Usuario", foreign_keys=[id_responsable], back_populates="tickets_gestionados")
    tecnico_asignado = relationship("Usuario", foreign_keys=[id_asignado], back_populates="tickets_asignados")