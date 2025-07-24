# app/schemas/projeto.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

# Schema base
class ProjetoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    status: Optional[str] = 'PLANEJAMENTO'
    cliente_id: Optional[int] = None
    data_inicio: Optional[datetime.date] = None
    data_fim_prevista: Optional[datetime.date] = None

# Schema para criar um novo projeto
class ProjetoCreate(ProjetoBase):
    pass

# Schema para atualizar um projeto
class ProjetoUpdate(ProjetoBase):
    pass

# Schema para retornar dados de um projeto pela API
class Projeto(ProjetoBase):
    id: int
    data_criacao: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
