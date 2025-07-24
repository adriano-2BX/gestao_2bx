# app/schemas/fluxo_automacao.py
from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any

class FluxoAutomacaoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    ferramenta: Optional[str] = None
    url_edicao: Optional[str] = None
    workflow_json: Optional[Dict[str, Any]] = None

class FluxoAutomacaoCreate(FluxoAutomacaoBase):
    pass

class FluxoAutomacaoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    ferramenta: Optional[str] = None
    url_edicao: Optional[str] = None
    workflow_json: Optional[Dict[str, Any]] = None

class FluxoAutomacao(FluxoAutomacaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
