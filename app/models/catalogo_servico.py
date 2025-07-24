from sqlalchemy import Column, Integer, String, TEXT
from ..core.db import Base
class CatalogoServico(Base):
    __tablename__ = "catalogo_servicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(TEXT)
