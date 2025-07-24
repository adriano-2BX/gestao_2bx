# app/models/certificado_ssl.py
from sqlalchemy import Column, Integer, String, DATE, Enum, DECIMAL
from ..core.db import Base

class CertificadoSSL(Base):
    __tablename__ = "certificados_ssl"

    id = Column(Integer, primary_key=True, index=True)
    nome_amigavel = Column(String(255), nullable=False)
    provedor_certificado = Column(String(100))
    # CORREÇÃO AQUI
    tipo_certificado = Column(Enum('DOMINIO_UNICO', 'WILDCARD', 'MULTIDOMINIO'), nullable=False)
    dominio_principal = Column(String(255), index=True)
    data_emissao = Column(DATE)
    data_expiracao = Column(DATE, nullable=False)
    custo_renovacao = Column(DECIMAL(10, 2))
