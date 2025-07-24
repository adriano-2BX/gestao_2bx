# app/models/dominio.py
from sqlalchemy import Column, Integer, String, DATE, Enum, DECIMAL, ForeignKey
from ..core.db import Base

class Dominio(Base):
    __tablename__ = "dominios"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo_fqdn = Column(String(255), unique=True, nullable=False, index=True)
    parent_id = Column(Integer, ForeignKey("dominios.id"))
    provedor_registro = Column(String(100))
    data_registro = Column(DATE)
    data_expiracao = Column(DATE, nullable=False)
    # CORREÇÃO AQUI
    status_dominio = Column(Enum('ATIVO', 'EXPIRADO', 'EM_REDENCAO', 'PENDENTE'), nullable=False, default='ATIVO')
    custo_anual_renovacao = Column(DECIMAL(10, 2))
