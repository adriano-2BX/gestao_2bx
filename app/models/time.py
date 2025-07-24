# app/models/time.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from ..core.db import Base

# Tabela de associação para a relação Muitos-para-Muitos entre Usuario e Time
usuario_time = Table(
    'usuario_time', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('time_id', Integer, ForeignKey('times.id'), primary_key=True)
)

class Time(Base):
    __tablename__ = "times"

    id = Column(Integer, primary_key=True, index=True)
    nome_time = Column(String(150), unique=True, nullable=False)
    descricao = Column(String(255))

    # Define o relacionamento com Usuario usando a tabela de associação
    usuarios = relationship("Usuario", secondary=usuario_time, back_populates="times")
