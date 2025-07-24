# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import (
    login,
    usuarios,
    papeis,
    permissoes,
    times,
    credenciais,
    clientes,
    projetos,
    tarefas,
    servidores,
    aplicacoes,
    dominios,
    certificados_ssl,
    conexoes,
    fluxos_automacao,
    instancias_api_whatsapp,
    numeros_whatsapp,
    timesheets # 1. Importe o novo endpoint
)

api_router = APIRouter()

# --- Rotas de Autenticação e Governança ---
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
# ... (outras rotas de governança)
api_router.include_router(credenciais.router, prefix="/credenciais", tags=["Cofre de Credenciais"])

# --- Rotas de Gestão de Projetos e Clientes ---
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])

# --- Rotas Financeiras e de Recursos ---
# 2. Adicione a nova rota
api_router.include_router(timesheets.router, prefix="/timesheets", tags=["Timesheets (Apontamento de Horas)"])

# --- Rotas de Infraestrutura e Ativos de TI ---
# ... (rotas de infraestrutura)
api_router.include_router(certificados_ssl.router, prefix="/certificados-ssl", tags=["Certificados SSL"])

# --- Rotas de Automação e Comunicação ---
# ... (rotas de automação)
api_router.include_router(numeros_whatsapp.router, prefix="/numeros-whatsapp", tags=["Números de WhatsApp"])

# --- Rota Estrutural de Conexões ---
api_-router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])
