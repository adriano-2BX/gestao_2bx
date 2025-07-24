# app/schemas/certificado_ssl.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class CertificadoSSLBase(BaseModel):
    nome_amigavel: str
    provedor_certificado: Optional[str] = None
    tipo_certificado: str
    dominio_principal: Optional[str] = None
    data_emissao: Optional[datetime.date] = None
    data_expiracao: datetime.date
    custo_renovacao: Optional[float] = None

class CertificadoSSLCreate(CertificadoSSLBase):
    pass

class CertificadoSSLUpdate(BaseModel):
    nome_amigavel: Optional[str] = None
    provedor_certificado: Optional[str] = None
    tipo_certificado: Optional[str] = None
    dominio_principal: Optional[str] = None
    data_emissao: Optional[datetime.date] = None
    data_expiracao: Optional[datetime.date] = None
    custo_renovacao: Optional[float] = None

class CertificadoSSL(CertificadoSSLBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
