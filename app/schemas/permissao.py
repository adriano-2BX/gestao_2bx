# app/schemas/permissao.py
from pydantic import BaseModel, ConfigDict

class PermissaoBase(BaseModel):
    nome: str

class PermissaoCreate(PermissaoBase):
    pass

class Permissao(PermissaoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
