# app/schemas/usuario.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UsuarioBase(BaseModel):
    email: EmailStr
    nome: str
    cargo: Optional[str] = None
    papel_id: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password: str # Recebe a senha em texto plano ao criar

class Usuario(UsuarioBase):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)
