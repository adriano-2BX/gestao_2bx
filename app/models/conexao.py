# app/models/conexao.py
from sqlalchemy import Column, Integer, String, BigInteger
from ..core.db import Base

class Conexao(Base):
    __tablename__ = "conexoes"

    id = Column(BigInteger, primary_key=True, index=True)
    origem_id = Column(Integer, nullable=False, index=True)
    origem_tabela = Column(String(100), nullable=False, index=True)
    destino_id = Column(Integer, nullable=False, index=True)
    destino_tabela = Column(String(100), nullable=False, index=True)
    tipo_relacionamento = Column(String(100), nullable=False)
