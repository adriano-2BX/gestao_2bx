# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import (
    login, usuarios, papeis, permissoes, times, credenciais,
    clientes, projetos, tarefas, servidores, aplicacoes, dominios,
    certificados_ssl, conexoes, fluxos_automacao,
    instancias_api_whatsapp, numeros_whatsapp, timesheets,
    catalogo_servicos, assinaturas, faturas # 1. Importe os novos endpoints
)

api_router = APIRouter()

# --- Rotas de Autenticação e Governança ---
# ... (rotas existentes)
api_router.include_router(credenciais.router, prefix="/credenciais", tags=["Cofre de Credenciais"])

# --- Rotas de Gestão de Projetos e Clientes ---
# ... (rotas existentes)
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])

# --- Rotas Financeiras e de Recursos ---
api_router.include_router(timesheets.router, prefix="/timesheets", tags=["Timesheets (Apontamento de Horas)"])
# 2. Adicione as novas rotas financeiras
api_router.include_router(catalogo_servicos.router, prefix="/catalogo-servicos", tags=["Catálogo de Serviços"])
api_router.include_router(assinaturas.router, prefix="/assinaturas", tags=["Assinaturas"])
api_router.include_router(faturas.router, prefix="/faturas", tags=["Faturas"])

# --- Rotas de Infraestrutura e Ativos de TI ---
# ... (rotas existentes)
api_router.include_router(certificados_ssl.router, prefix="/certificados-ssl", tags=["Certificados SSL"])

# --- Rotas de Automação e Comunicação ---
# ... (rotas existentes)
api_router.include_router(numeros_whatsapp.router, prefix="/numeros-whatsapp", tags=["Números de WhatsApp"])

# --- Rota Estrutural de Conexões ---
api_router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])
