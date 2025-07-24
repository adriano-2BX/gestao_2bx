# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import (
    clientes, projetos, tarefas, 
    usuarios, login, servidores, 
    aplicacoes, dominios, certificados_ssl # 1. Importe 'certificados_ssl'
)

api_router = APIRouter()

# Rota de autenticação
api_router.include_router(login.router, tags=["Login"])

# Rotas de recursos
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
api_router.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
api_router.include_router(servidores.router, prefix="/servidores", tags=["Servidores"])
api_router.include_router(aplicacoes.router, prefix="/aplicacoes", tags=["Aplicações"])
api_router.include_router(dominios.router, prefix="/dominios", tags=["Domínios"])

# 2. Adicione a nova rota de Certificados SSL
api_router.include_router(certificados_ssl.router, prefix="/certificados-ssl", tags=["Certificados SSL"])
# Rota Estrutural de Conexões
# 2. Adicione a nova rota de Conexões
api_router.include_router(conexoes.router, prefix="/conexoes", tags=["Conexões"])
