from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketBase(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str
    id_laboratorio: int
    id_servicio: int

class TicketCreate(TicketBase):
    id_solicitante: int

class TicketUpdateEstado(BaseModel):
    estado: str

class TicketOut(TicketBase):
    id_ticket: int
    id_solicitante: int
    id_responsable: Optional[int]
    id_asignado: Optional[int]
    estado: str
    fecha_creacion: datetime
    class Config: from_attributes = True