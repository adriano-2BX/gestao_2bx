# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import clientes, projetos, tarefas # 1. Importe 'tarefas'

api_router = APIRouter()

api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])

# 2. Adicione a nova rota de Tarefas
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])
