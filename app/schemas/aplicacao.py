# app/schemas/aplicacao.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

class AplicacaoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    url_repositorio: Optional[str] = None
    linguagem: Optional[str] = None

class AplicacaoCreate(AplicacaoBase):
    pass

class AplicacaoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    url_repositorio: Optional[str] = None
    linguagem: Optional[str] = None

class Aplicacao(AplicacaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
