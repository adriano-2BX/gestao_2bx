import os
from fastapi import FastAPI

# --- INÍCIO DO CÓDIGO DE DEPURAÇÃO ---

print("==================================================")
print("INICIANDO SESSÃO DE DEPURAÇÃO DE IMPORTS")
print("==================================================")

def debug_file(path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), path)
        print(f"\n[DEBUG] Verificando o arquivo: {full_path}")
        if not os.path.exists(full_path):
            print(f"[ERRO] O arquivo não foi encontrado!")
            return

        with open(full_path, "r") as f:
            content = f.read().strip()

        if not content:
            print("[AVISO] O conteúdo do arquivo está VAZIO.")
        else:
            print(f"[CONTEÚDO]\n---\n{content}\n---")

    except Exception as e:
        print(f"[ERRO GERAL] Falha ao ler o arquivo: {e}")

# Verificando os arquivos críticos
debug_file("schemas/__init__.py")
debug_file("models/__init__.py")

print("\n[DEBUG] Tentando importar o api_router...")
try:
    from .api.api_router import api_router
    print("[SUCESSO] O api_router foi importado com sucesso.")
except Exception as e:
    print(f"[ERRO FATAL] Falha ao importar o api_router. Erro original abaixo:")
    # Isso irá printar o erro original que estamos vendo
    raise e

print("==================================================")
print("FIM DA SESSÃO DE DEPURAÇÃO")
print("==================================================")

# --- FIM DO CÓDIGO DE DEPURAÇÃO ---


# O código original da aplicação
app = FastAPI(
    title="API de Gestão Integrada",
    description="A API central para gestão de todos os ativos e operações.",
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Gestão Integrada!"}
