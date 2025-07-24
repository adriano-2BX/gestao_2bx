# app/schemas/credencial.py
from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
import datetime

# Schema para visualização (NÃO expõe segredos)
class Credencial(BaseModel):
    id: int
    nome: str
    tipo_credencial: str
    data_criacao: datetime.datetime
    model_config = ConfigDict(from_attributes=True)

# Schema para criação (recebe dados em texto plano)
class CredencialCreate(BaseModel):
    nome: str
    tipo_credencial: str
    dados_credencial: Dict[str, Any]
    notas_seguras: Optional[str] = None

# Schema para atualização
class CredencialUpdate(BaseModel):
    nome: Optional[str] = None
    tipo_credencial: Optional[str] = None
    dados_credencial: Optional[Dict[str, Any]] = None
    notas_seguras: Optional[str] = None

# Schema para a resposta da rota /revelar
class CredencialRevelada(BaseModel):
    dados_credencial: Dict[str, Any]
    notas_seguras: Optional[str] = None
