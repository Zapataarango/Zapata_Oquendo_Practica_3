from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class TicketBase(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str
    id_laboratorio: int
    id_servicio: int

class TicketCreate(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str
    id_laboratorio: int
    id_servicio: int
    id_solicitante: int

class TicketUpdateEstado(BaseModel):
    nuevo_estado: str

class TicketOut(TicketBase):
    id_ticket: int
    id_solicitante: int
    id_responsable: Optional[int]
    id_asignado: Optional[int]
    estado: str
    fecha_creacion: datetime
    class Config: from_attributes = True

from pydantic import BaseModel, Field

class TicketAsignar(BaseModel):
    id_asignado: int = Field(..., description="ID del técnico o auxiliar responsable")

    model_config = {
        "json_schema_extra": {
            "example": {"id_asignado": 10}
        }
    }