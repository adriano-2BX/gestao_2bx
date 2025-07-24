# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import clientes, projetos, tarefas, usuarios # 1. Importe 'usuarios'

api_router = APIRouter()

api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])

# 2. Adicione a nova rota de Usuários
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
