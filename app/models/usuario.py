# app/models/usuario.py
from sqlalchemy import Column, Integer, String, ENUM, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship # Importe 'relationship'
from sqlalchemy.sql import func
from ..core.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email # app/models/usuario.py
from sqlalchemy import Column, Integer, String, ENUM, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.db import Base
from .time import usuario_time # Importe a tabela de associação

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

    papel = relationship("Papel")

    # Adicione este relacionamento para conectar Usuario a Time
    times = relationship("Time", secondary=usuario_time, back_populates="usuarios")= Column(String(255), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    cargo = Column(String(150))
    status = Column(ENUM('ATIVO', 'INATIVO', 'PENDENTE'), nullable=False, default='PENDENTE')
    papel_id = Column(Integer, ForeignKey("papeis.id"))
    data_criacao = Column(TIMESTAMP, server_default=func.now())

    # Linha adicionada para criar o relacionamento com a tabela de papéis
    papel = relationship("Papel")
