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
    timesheets,
    catalogo_servicos,
    assinaturas,
    faturas,
    llm_modelos,
    llm_precos,
    llm_custos
)

api_router = APIRouter()

# --- Rotas de Autenticação e Governança ---
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
api_router.include_router(papeis.router, prefix="/papeis", tags=["Papéis (Roles)"])
api_router.include_router(permissoes.router, prefix="/permissoes", tags=["Permissões"])
api_router.include_router(times.router, prefix="/times", tags=["Times"])
api_router.include_router(credenciais.router, prefix="/credenciais", tags=["Cofre de Credenciais"])

# --- Rotas de Gestão de Projetos e Clientes ---
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])

# --- Rotas Financeiras e de Recursos ---
api_router.include_router(timesheets.router, prefix="/timesheets", tags=["Timesheets (Apontamento de Horas)"])
api_router.include_router(catalogo_servicos.router, prefix="/catalogo-servicos", tags=["Catálogo de Serviços"])
api_router.include_router(assinaturas.router, prefix="/assinaturas", tags=["Assinaturas"])
api_router.include_router(faturas.router, prefix="/faturas", tags=["Faturas"])

# --- Rotas de Infraestrutura e Ativos de TI ---
api_router.include_router(servidores.router, prefix="/servidores", tags=["Servidores"])
api_router.include_router(aplicacoes.router, prefix="/aplicacoes", tags=["Aplicações"])
api_router.include_router(dominios.router, prefix="/dominios", tags=["Domínios"])
api_router.include_router(certificados_ssl.router, prefix="/certificados-ssl", tags=["Certificados SSL"])

# --- Rotas de Automação e Comunicação ---
api_router.include_router(fluxos_automacao.router, prefix="/fluxos-automacao", tags=["Fluxos de Automação"])
api_router.include_router(instancias_api_whatsapp.router, prefix="/instancias-api-whatsapp", tags=["Instâncias API WhatsApp"])
api_router.include_router(numeros_whatsapp.router, prefix="/numeros-whatsapp", tags=["Números de WhatsApp"])

# --- Rotas de Gestão de IA (LLMs) ---
api_router.include_router(llm_modelos.router, prefix="/llm/modelos", tags=["LLM - Modelos"])
api_router.include_router(llm_precos.router, prefix="/llm/precos", tags=["LLM - Preços"])
api_router.include_router(llm_custos.router, prefix="/llm/custos", tags=["LLM - Custos e Uso"])

# --- Rota Estrutural de Conexões ---
api_router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])

# A linha com o erro de indentação que estava aqui foi removida.
