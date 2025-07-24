# app/schemas/papel.py
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .permissao import Permissao

class PapelBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class PapelCreate(PapelBase):
    pass

class PapelUpdate(PapelBase):
    pass

class Papel(PapelBase):
    id: int
    permissoes: List[Permissao] = []
    model_config = ConfigDict(from_attributes=True)

class LinkPermissaoToPapel(BaseModel):
    permissao_id: int
