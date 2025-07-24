# app/models/aplicacao.py
from sqlalchemy import Column, Integer, String, TEXT
from ..core.db import Base

class Aplicacao(Base):
    __tablename__ = "aplicacoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False, index=True)
    descricao = Column(TEXT)
    url_repositorio = Column(String(255))
    linguagem = Column(String(100))
