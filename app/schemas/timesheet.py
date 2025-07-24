# app/schemas/timesheet.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class TimesheetBase(BaseModel):
    data: datetime.date
    horas_gastas: float
    tarefa_id: Optional[int] = None
    descricao_atividade: Optional[str] = None

class TimesheetCreate(TimesheetBase):
    pass

class TimesheetUpdate(BaseModel):
    data: Optional[datetime.date] = None
    horas_gastas: Optional[float] = None
    tarefa_id: Optional[int] = None
    descricao_atividade: Optional[str] = None

# Schema de resposta, mais rico, para devolvermos no GET
class Timesheet(TimesheetBase):
    id: int
    usuario_id: int

    model_config = ConfigDict(from_attributes=True)
