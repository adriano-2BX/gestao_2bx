from pydantic import BaseModel, ConfigDict
from typing import Optional
class LLMModeloBase(BaseModel):
    nome_modelo_api: str
    nome_amigavel: Optional[str] = None
    provedor: str
class LLMModeloCreate(LLMModeloBase):
    pass
class LLMModelo(LLMModeloBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
