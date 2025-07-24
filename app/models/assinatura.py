# app/models/assinatura.py
from sqlalchemy import Column, Integer, String, Enum, DATE, DECIMAL, ForeignKey
from ..core.db import Base
class Assinatura(Base):
    __tablename__ = "assinaturas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("catalogo_servicos.id"), nullable=False)
    valor_recorrente = Column(DECIMAL(10, 2), nullable=False)
    # CORREÇÃO AQUI
    ciclo_cobranca = Column(Enum('MENSAL', 'TRIMESTRAL', 'ANUAL'), nullable=False)
    # CORREÇÃO AQUI
    status = Column(Enum('ATIVA', 'CANCELADA', 'INADIMPLENTE', 'TESTE'), nullable=False)
    data_inicio = Column(DATE, nullable=False)
    data_proxima_cobranca = Column(DATE, nullable=False)
