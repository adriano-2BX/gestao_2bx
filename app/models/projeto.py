# app/models/projeto.py
from sqlalchemy import Column, Integer, String, TEXT, ENUM, DATE, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from ..core.db import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(TEXT)
    status = Column(ENUM('PLANEJAMENTO', 'EM_ANDAMENTO', 'CONCLUIDO', 'CANCELADO', 'EM_ESPERA'), nullable=False, default='PLANEJAMENTO')
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    data_inicio = Column(DATE)
    data_fim_prevista = Column(DATE)
    data_criacao = Column(TIMESTAMP, server_default=func.now())
