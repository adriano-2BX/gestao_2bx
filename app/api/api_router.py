# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import clientes, projetos, tarefas, usuarios, login # 1. Importe 'login'

api_router = APIRouter()

# Rota de autenticação
api_router.include_router(login.router, tags=["Login"])

# Rotas de recursos
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
