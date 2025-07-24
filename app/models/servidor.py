# app/models/servidor.py
from sqlalchemy import Column, Integer, String, TEXT, Enum
from ..core.db import Base

class Servidor(Base):
    __tablename__ = "servidores"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(255), unique=True, nullable=False, index=True)
    ip_principal = Column(String(45))
    sistema_operacional = Column(String(100))
    descricao = Column(TEXT)
    status = Column(Enum('ATIVO', 'INATIVO', 'MANUTENCAO', 'FALHA'), nullable=False, default='ATIVO')
