# app/models/timesheet.py
from sqlalchemy import Column, Integer, BigInteger, DECIMAL, DATE, TEXT, ForeignKey
from sqlalchemy.orm import relationship
from ..core.db import Base

class Timesheet(Base):
    __tablename__ = "timesheets"

    id = Column(BigInteger, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tarefa_id = Column(Integer, ForeignKey("tarefas.id")) # Pode ser nulo, para apontar horas no projeto em geral
    data = Column(DATE, nullable=False)
    horas_gastas = Column(DECIMAL(5, 2), nullable=False)
    descricao_atividade = Column(TEXT)

    # Relacionamentos para facilitar o acesso aos dados
    usuario = relationship("Usuario")
    tarefa = relationship("Tarefa")
