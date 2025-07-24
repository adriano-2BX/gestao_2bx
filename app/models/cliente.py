# app/models/cliente.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from ..core.db import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cnpj_cpf = Column(String(20), unique=True, index=True)
    contato_principal = Column(String(255))
    email = Column(String(255))
    telefone = Column(String(20))
    data_criacao = Column(TIMESTAMP, server_default=func.now())
