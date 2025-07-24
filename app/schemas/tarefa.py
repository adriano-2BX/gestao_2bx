# app/schemas/tarefa.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: Optional[str] = 'A_FAZER'
    projeto_id: int
    responsavel_id: Optional[int] = None
    data_entrega: Optional[datetime.date] = None
    prioridade: Optional[str] = 'MEDIA'

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
    responsavel_id: Optional[int] = None
    data_entrega: Optional[datetime.date] = None
    prioridade: Optional[str] = None

class Tarefa(TarefaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
