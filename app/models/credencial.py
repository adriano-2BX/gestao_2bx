# app/models/credencial.py
from sqlalchemy import Column, Integer, String, ENUM, TEXT, TIMESTAMP
from sqlalchemy.sql import func
from ..core.db import Base

class Credencial(Base):
    __tablename__ = "credenciais"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    tipo_credencial = Column(ENUM('API_KEY', 'USUARIO_SENHA', 'TOKEN_JWT', 'CHAVE_SSH_PRIVADA', 'CERTIFICADO', 'OUTRO'), nullable=False)
    dados_credencial_encrypted = Column(TEXT, nullable=False)
    notas_seguras_encrypted = Column(TEXT)
    data_criacao = Column(TIMESTAMP, server_default=func.now())
