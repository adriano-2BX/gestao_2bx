# app/models/instancia_api_whatsapp.py
from sqlalchemy import Column, Integer, String, ENUM
from ..core.db import Base

class InstanciaAPIWhatsApp(Base):
    __tablename__ = "instancias_api_whatsapp"

    id = Column(Integer, primary_key=True, index=True)
    nome_instancia = Column(String(255), nullable=False)
    tipo_api = Column(ENUM('EVOLUTION', 'META_BUSINESS', 'WAHA', 'Z_API', 'OUTRO'), nullable=False)
    endpoint_url = Column(String(255))
    status_instancia = Column(ENUM('OPERACIONAL', 'FALHA', 'MANUTENCAO'), nullable=False, default='OPERACIONAL')
