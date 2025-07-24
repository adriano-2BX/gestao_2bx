from sqlalchemy import Column, Integer, DECIMAL, DATE, ForeignKey
from ..core.db import Base
class LLMPreco(Base):
    __tablename__ = "llm_precos_modelos"
    id = Column(Integer, primary_key=True, index=True)
    modelo_id = Column(Integer, ForeignKey("llm_modelos.id"), nullable=False)
    preco_milhao_tokens_entrada = Column(DECIMAL(10, 4), nullable=False)
    preco_milhao_tokens_saida = Column(DECIMAL(10, 4), nullable=False)
    data_vigor = Column(DATE, nullable=False)
