# app/models/llm_modelo.py
from sqlalchemy import Column, Integer, String, Enum
from ..core.db import Base
class LLMModelo(Base):
    __tablename__ = "llm_modelos"
    id = Column(Integer, primary_key=True, index=True)
    nome_modelo_api = Column(String(100), unique=True, nullable=False)
    nome_amigavel = Column(String(100))
    # CORREÇÃO AQUI
    provedor = Column(Enum('OPENAI', 'GOOGLE_AI', 'ANTHROPIC', 'AZURE_OPENAI', 'HUGGING_FACE', 'SELF_HOSTED'), nullable=False)
