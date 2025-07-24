# app/schemas/numero_whatsapp.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

class NumeroWhatsAppBase(BaseModel):
    numero: str
    nome_associado: Optional[str] = None
    descricao_uso: Optional[str] = None
    status_numero: Optional[str] = 'ATIVO'

class NumeroWhatsAppCreate(NumeroWhatsAppBase):
    pass

class NumeroWhatsAppUpdate(BaseModel):
    numero: Optional[str] = None
    nome_associado: Optional[str] = None
    descricao_uso: Optional[str] = None
    status_numero: Optional[str] = None

class NumeroWhatsApp(NumeroWhatsAppBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
