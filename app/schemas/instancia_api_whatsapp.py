# app/schemas/instancia_api_whatsapp.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

class InstanciaAPIWhatsAppBase(BaseModel):
    nome_instancia: str
    tipo_api: str
    endpoint_url: Optional[str] = None
    status_instancia: Optional[str] = 'OPERACIONAL'

class InstanciaAPIWhatsAppCreate(InstanciaAPIWhatsAppBase):
    pass

class InstanciaAPIWhatsAppUpdate(BaseModel):
    nome_instancia: Optional[str] = None
    tipo_api: Optional[str] = None
    endpoint_url: Optional[str] = None
    status_instancia: Optional[str] = None

class InstanciaAPIWhatsApp(InstanciaAPIWhatsAppBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
