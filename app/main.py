# app/main.py
from fastapi import FastAPI
from .api.api_router import api_router

app = FastAPI(
    title="API de Gestão Integrada",
    description="A API central para gestão de todos os ativos e operações.",
    version="0.1.0"
)

# Inclui todas as rotas da API sob o prefixo /api/v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/", summary="Rota Raiz")
def read_root():
    """
    Rota raiz da aplicação que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API de Gestão Integrada!"}
