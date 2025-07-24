# app/models/fluxo_automacao.py
from sqlalchemy import Column, Integer, String, TEXT, JSON
from ..core.db import Base

class FluxoAutomacao(Base):
    __tablename__ = "fluxos_automacao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False, index=True)
    descricao = Column(TEXT)
    ferramenta = Column(String(100))
    url_edicao = Column(String(255))
    workflow_json = Column(JSON)
