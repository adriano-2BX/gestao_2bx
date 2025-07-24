# app/models/tarefa.py
from sqlalchemy import Column, Integer, String, TEXT, Enum, DATE, ForeignKey
from ..core.db import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(TEXT)
    status = Column(Enum('A_FAZER', 'EM_ANDAMENTO', 'CONCLUIDA', 'BLOQUEADA'), nullable=False, default='A_FAZER')
    projeto_id = Column(Integer, ForeignKey("projetos.id"), nullable=False)
    responsavel_id = Column(Integer, ForeignKey("usuarios.id"))
    data_entrega = Column(DATE)
    prioridade = Column(Enum('BAIXA', 'MEDIA', 'ALTA', 'URGENTE'), nullable=False, default='MEDIA')
