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
    numeros_whatsapp # 1. Importe o novo endpoint
)

api_router = APIRouter()

# --- Rotas de Autenticação e Governança ---
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
api_router.include_router(papeis.router, prefix="/papeis", tags=["Papéis (Roles)"])
api_router.include_router(permissoes.router, prefix="/permissoes", tags=["Permissões"])
api_router.include_router(times.router, prefix="/times", tags=["Times"])
api_router.include_router(credenciais.router, prefix="/credenciais", tags=["Cofre de Credenciais"])

# --- Rotas de Gestão de Projetos e Clientes ---
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])

# --- Rotas de Infraestrutura e Ativos de TI ---
api_router.include_router(servidores.router, prefix="/servidores", tags=["Servidores"])
api_router.include_router(aplicacoes.router, prefix="/aplicacoes", tags=["Aplicações"])
api_router.include_router(dominios.router, prefix="/dominios", tags=["Domínios"])
api_router.include_router(certificados_ssl.router, prefix="/certificados-ssl", tags=["Certificados SSL"])

# --- Rotas de Automação e Comunicação ---
api_router.include_router(fluxos_automacao.router, prefix="/fluxos-automacao", tags=["Fluxos de Automação"])
api_router.include_router(instancias_api_whatsapp.router, prefix="/instancias-api-whatsapp", tags=["Instâncias API WhatsApp"])
# 2. Adicione a nova rota
api_router.include_router(numeros_whatsapp.router, prefix="/numeros-whatsapp", tags=["Números de WhatsApp"])

# --- Rota Estrutural de Conexões ---
api_router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])
