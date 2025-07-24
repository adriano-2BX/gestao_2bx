# app/models/fatura.py
from sqlalchemy import Column, Integer, String, Enum, DATE, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..core.db import Base
class Fatura(Base):
    __tablename__ = "faturas"
    id = Column(Integer, primary_key=True, index=True)
    assinatura_id = Column(Integer, ForeignKey("assinaturas.id"))
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    valor_total = Column(DECIMAL(10, 2), nullable=False)
    data_emissao = Column(DATE, nullable=False)
    data_vencimento = Column(DATE, nullable=False)
    data_pagamento = Column(DATE)
    # CORREÇÃO AQUI
    status = Column(Enum('PENDENTE', 'PAGA', 'VENCIDA', 'CANCELADA'), nullable=False)
    itens = relationship("ItemFatura", back_populates="fatura")
#... (o resto do arquivo ItemFatura permanece igual)
