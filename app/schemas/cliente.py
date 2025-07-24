# app/schemas/cliente.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
import datetime

# Schema base com campos comuns
class ClienteBase(BaseModel):
    nome: str
    cnpj_cpf: Optional[str] = None
    contato_principal: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

# Schema para criação de um novo cliente
class ClienteCreate(ClienteBase):
    pass

# Schema para atualização de um cliente
class ClienteUpdate(ClienteBase):
    pass

# Schema para leitura (retorno da API)
class Cliente(ClienteBase):
    id: int
    data_criacao: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
