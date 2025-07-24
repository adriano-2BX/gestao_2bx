# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import (
    login, usuarios, papeis, permissoes, times, credenciais,
    clientes, projetos, tarefas, servidores, aplicacoes, dominios,
    certificados_ssl, conexoes, fluxos_automacao,
    instancias_api_whatsapp, numeros_whatsapp, timesheets,
    catalogo_servicos, assinaturas, faturas,
    llm_modelos, llm_precos, llm_custos # 1. Importe os novos endpoints
)

api_router = APIRouter()

# --- Rotas de Autenticação e Governança ---
# ... (rotas existentes)
api_router.include_router(credenciais.router, prefix="/credenciais", tags=["Cofre de Credenciais"])

# --- Rotas de Gestão de Projetos e Clientes ---
# ... (rotas existentes)

# --- Rotas Financeiras e de Recursos ---
# ... (rotas existentes)
api_router.include_router(faturas.router, prefix="/faturas", tags=["Faturas"])

# --- Rotas de Infraestrutura e Ativos de TI ---
# ... (rotas existentes)

# --- Rotas de Automação e Comunicação ---
# ... (rotas existentes)

# --- Rotas de Gestão de IA (LLMs) ---
# 2. Adicione as novas rotas
api_router.include_router(llm_modelos.router, prefix="/llm/modelos", tags=["LLM - Modelos"])
api_router.include_router(llm_precos.router, prefix="/llm/precos", tags=["LLM - Preços"])
api_router.include_router(llm_custos.router, prefix="/llm/custos", tags=["LLM - Custos e Uso"])

# --- Rota Estrutural de Conexões ---
api_router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])
