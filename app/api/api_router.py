# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import clientes, projetos # 1. Importe 'projetos'

api_router = APIRouter()

# Rota de Clientes (já existia)
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])

# 2. Adicione a nova rota de Projetos
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
