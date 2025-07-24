from sqlalchemy import Column, Integer, BigInteger, DECIMAL, TIMESTAMP, ForeignKey
from ..core.db import Base
class LLMCustoUso(Base):
    __tablename__ = "llm_custos_uso"
    id = Column(BigInteger, primary_key=True, index=True)
    timestamp_chamada = Column(TIMESTAMP, nullable=False)
    credencial_id = Column(Integer, ForeignKey("credenciais.id"), nullable=False)
    modelo_id = Column(Integer, ForeignKey("llm_modelos.id"), nullable=False)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    tokens_entrada = Column(Integer, nullable=False)
    tokens_saida = Column(Integer, nullable=False)
    custo_calculado = Column(DECIMAL(10, 6), nullable=False)
