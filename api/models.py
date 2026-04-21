from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from src.domain.enums import PrioridadTarea

class UsuarioCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    
class UsuarioResponse(BaseModel):
    username: str
    email: str
    activo: bool

class ProyectoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    descripcion: Optional[str] = None

class TareaCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=50)
    prioridad: PrioridadTarea = Field(default=PrioridadTarea.MEDIA)

class TareaUpdate(BaseModel):
    prioridad: Optional[PrioridadTarea] = None
    completada: Optional[bool] = None