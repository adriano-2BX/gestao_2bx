# app/models/papel.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from ..core.db import Base

# Tabela de associação para a relação Muitos-para-Muitos entre Papel e Permissao
papel_permissoes = Table(
    'papel_permissoes', Base.metadata,
    Column('papel_id', Integer, ForeignKey('papeis.id'), primary_key=True),
    Column('permissao_id', Integer, ForeignKey('permissoes.id'), primary_key=True)
)

class Papel(Base):
    __tablename__ = "papeis"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True, nullable=False)
    descricao = Column(String(255))

    # Define o relacionamento com Permissao usando a tabela de associação
    permissoes = relationship("Permissao", secondary=papel_permissoes)

class Permissao(Base):
    __tablename__ = "permissoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True, nullable=False) # ex: "projeto:criar", "cliente:ver"
