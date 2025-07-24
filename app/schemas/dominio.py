# app/schemas/dominio.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class DominioBase(BaseModel):
    nome_completo_fqdn: str
    parent_id: Optional[int] = None
    provedor_registro: Optional[str] = None
    data_registro: Optional[datetime.date] = None
    data_expiracao: datetime.date
    status_dominio: Optional[str] = 'ATIVO'
    custo_anual_renovacao: Optional[float] = None

class DominioCreate(DominioBase):
    pass

class DominioUpdate(BaseModel):
    nome_completo_fqdn: Optional[str] = None
    parent_id: Optional[int] = None
    provedor_registro: Optional[str] = None
    data_registro: Optional[datetime.date] = None
    data_expiracao: Optional[datetime.date] = None
    status_dominio: Optional[str] = None
    custo_anual_renovacao: Optional[float] = None

class Dominio(DominioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
