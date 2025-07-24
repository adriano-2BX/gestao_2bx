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
    status = Column(Enum('PENDENTE', 'PAGA', 'VENCIDA', 'CANCELADA'), nullable=False)

    # Define a relação "um-para-muitos": uma fatura tem muitos itens
    itens = relationship("ItemFatura", back_populates="fatura", cascade="all, delete-orphan")

class ItemFatura(Base):
    __tablename__ = "itens_fatura"

    id = Column(Integer, primary_key=True, index=True)
    fatura_id = Column(Integer, ForeignKey("faturas.id"), nullable=False)
    descricao = Column(String(255), nullable=False)
    quantidade = Column(DECIMAL(10, 2), nullable=False)
    valor_unitario = Column(DECIMAL(10, 2), nullable=False)
    valor_total_item = Column(DECIMAL(10, 2), nullable=False)

    # Define a relação "muitos-para-um": um item pertence a uma fatura
    fatura = relationship("Fatura", back_populates="itens")
