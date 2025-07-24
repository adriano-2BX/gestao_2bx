from pydantic import BaseModel, ConfigDict
from typing import Optional
class CatalogoServicoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
class CatalogoServicoCreate(CatalogoServicoBase):
    pass
class CatalogoServico(CatalogoServicoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
