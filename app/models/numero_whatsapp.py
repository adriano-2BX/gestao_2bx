# app/models/numero_whatsapp.py
from sqlalchemy import Column, Integer, String, Enum, TEXT
from ..core.db import Base

class NumeroWhatsApp(Base):
    __tablename__ = "numeros_whatsapp"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(20), unique=True, nullable=False, index=True)
    nome_associado = Column(String(100))
    descricao_uso = Column(TEXT)
    # CORREÇÃO AQUI
    status_numero = Column(Enum('ATIVO', 'INATIVO', 'BANIDO', 'EM_AQUECIMENTO', 'AGUARDANDO_CONEXAO'), nullable=False, default='ATIVO')
