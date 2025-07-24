# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. Importe o CORSMiddleware
from .api.api_router import api_router

app = FastAPI(
    title="API de Gestão Integrada",
    description="A API central para gestão de todos os ativos e operações.",
    version="0.1.0"
)

# 2. Adicione a configuração do CORS
# Esta configuração permite que qualquer origem (*) acesse sua API.
# É seguro para começar, mas em produção você pode restringir para domínios específicos.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# O resto do seu código permanece o mesmo
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    """
    Rota raiz da aplicação que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API de Gestão Integrada!"}
