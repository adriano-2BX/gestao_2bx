from pydantic import BaseModel, ConfigDict
from typing import Optional, List
import datetime
class ItemFaturaBase(BaseModel):
    descricao: str
    quantidade: float
    valor_unitario: float
    valor_total_item: float
class ItemFatura(ItemFaturaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
class FaturaBase(BaseModel):
    cliente_id: int
    assinatura_id: Optional[int] = None
    valor_total: float
    data_emissao: datetime.date
    data_vencimento: datetime.date
    data_pagamento: Optional[datetime.date] = None
    status: str
class Fatura(FaturaBase):
    id: int
    itens: List[ItemFatura] = []
    model_config = ConfigDict(from_attributes=True)
