from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime
class LLMCustoUsoBase(BaseModel):
    credencial_id: int
    modelo_id: int
    projeto_id: Optional[int] = None
    tokens_entrada: int
    tokens_saida: int
class LLMCustoUsoCreate(LLMCustoUsoBase):
    pass
class LLMCustoUso(LLMCustoUsoBase):
    id: int
    timestamp_chamada: datetime.datetime
    custo_calculado: float
    model_config = ConfigDict(from_attributes=True)
