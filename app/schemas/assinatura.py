from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime
class AssinaturaBase(BaseModel):
    cliente_id: int
    servico_id: int
    valor_recorrente: float
    ciclo_cobranca: str
    status: str
    data_inicio: datetime.date
    data_proxima_cobranca: datetime.date
class AssinaturaCreate(AssinaturaBase):
    pass
class Assinatura(AssinaturaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
