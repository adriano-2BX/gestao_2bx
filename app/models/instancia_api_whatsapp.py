# app/models/instancia_api_whatsapp.py
from sqlalchemy import Column, Integer, String, Enum
from ..core.db import Base

class InstanciaAPIWhatsApp(Base):
    __tablename__ = "instancias_api_whatsapp"

    id = Column(Integer, primary_key=True, index=True)
    nome_instancia = Column(String(255), nullable=False)
    # CORREÇÃO AQUI
    tipo_api = Column(Enum('EVOLUTION', 'META_BUSINESS', 'WAHA', 'Z_API', 'OUTRO'), nullable=False)
    endpoint_url = Column(String(255))
    # CORREÇÃO AQUI
    status_instancia = Column(Enum('OPERACIONAL', 'FALHA', 'MANUTENCAO'), nullable=False, default='OPERACIONAL')
