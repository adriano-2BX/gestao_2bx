# app/schemas/time.py
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .usuario import Usuario # Reutilizamos o schema de Usuário

class TimeBase(BaseModel):
    nome_time: str
    descricao: Optional[str] = None

class TimeCreate(TimeBase):
    pass

class TimeUpdate(TimeBase):
    pass

# Schema para resposta, incluindo a lista de membros
class Time(TimeBase):
    id: int
    usuarios: List[Usuario] = []

    model_config = ConfigDict(from_attributes=True)

class LinkUsuarioToTime(BaseModel):
    usuario_id: int
