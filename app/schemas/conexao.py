# app/schemas/conexao.py
from pydantic import BaseModel, ConfigDict

class ConexaoBase(BaseModel):
    origem_id: int
    origem_tabela: str
    destino_id: int
    destino_tabela: str
    tipo_relacionamento: str

class ConexaoCreate(ConexaoBase):
    pass

class Conexao(ConexaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
