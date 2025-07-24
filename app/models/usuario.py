# app/models/usuario.py
# CORREÇÃO 1: Importar 'Enum' com 'E' maiúsculo
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.db import Base
from .time import usuario_time

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    cargo = Column(String(150))
    # CORREÇÃO 2: Usar 'Enum' com 'E' maiúsculo
    status = Column(Enum('ATIVO', 'INATIVO', 'PENDENTE'), nullable=False, default='PENDENTE')
    papel_id = Column(Integer, ForeignKey("papeis.id"))
    data_criacao = Column(TIMESTAMP, server_default=func.now())

    papel = relationship("Papel")

    times = relationship("Time", secondary=usuario_time, back_populates="usuarios")
