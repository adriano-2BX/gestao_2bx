# app/models/usuario.py
from sqlalchemy import Column, Integer, String, ENUM, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from ..core.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    cargo = Column(String(150))
    status = Column(ENUM('ATIVO', 'INATIVO', 'PENDENTE'), nullable=False, default='PENDENTE')
    papel_id = Column(Integer, ForeignKey("papeis.id"))
    data_criacao = Column(TIMESTAMP, server_default=func.now())
