from pydantic import BaseModel

class LaboratorioBase(BaseModel):
    nombre: str
    ubicacion: str

class LaboratorioCreate(LaboratorioBase):
    pass

class LaboratorioOut(LaboratorioBase):
    id_laboratorio: int
    activo: bool
    class Config: from_attributes = True
