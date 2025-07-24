from pydantic import BaseModel, ConfigDict
import datetime
class LLMPrecoBase(BaseModel):
    modelo_id: int
    preco_milhao_tokens_entrada: float
    preco_milhao_tokens_saida: float
    data_vigor: datetime.date
class LLMPrecoCreate(LLMPrecoBase):
    pass
class LLMPreco(LLMPrecoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
