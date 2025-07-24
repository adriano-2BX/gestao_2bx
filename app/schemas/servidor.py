# app/schemas/servidor.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

class ServidorBase(BaseModel):
    hostname: str
    ip_principal: Optional[str] = None
    sistema_operacional: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = 'ATIVO'

class ServidorCreate(ServidorBase):
    pass

class ServidorUpdate(BaseModel):
    hostname: Optional[str] = None
    ip_principal: Optional[str] = None
    sistema_operacional: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None

class Servidor(ServidorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
