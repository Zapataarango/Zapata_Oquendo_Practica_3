from pydantic import BaseModel
from typing import Optional

class ServicioBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class ServicioCreate(ServicioBase):
    pass

class ServicioOut(ServicioBase):
    id_servicio: int
    activo: bool
    class Config: from_attributes = True