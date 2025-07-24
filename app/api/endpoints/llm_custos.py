# app/api/endpoints/llm_custos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional # Adicione 'Optional' a esta linha de importação
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission
import datetime

router = APIRouter()

@router.post("/log-usage", response_model=schemas.LLMCustoUso, status_code=201, summary="Registra o uso de uma chamada de LLM e calcula o custo")
def log_llm_usage(
    usage: schemas.LLMCustoUsoCreate, 
    db: Session = Depends(get_db), 
    user: models.Usuario = Depends(require_permission("llm_custo:criar"))
):
    # 1. Encontrar o preço atual para o modelo
    preco_atual = db.query(models.LLMPreco).filter(models.LLMPreco.modelo_id == usage.modelo_id).order_by(models.LLMPreco.data_vigor.desc()).first()
    if not preco_atual:
        raise HTTPException(status_code=404, detail=f"Tabela de preços para o modelo id {usage.modelo_id} não encontrada.")

    # 2. Calcular o custo
    custo_entrada = (usage.tokens_entrada / 1_000_000) * float(preco_atual.preco_milhao_tokens_entrada)
    custo_saida = (usage.tokens_saida / 1_000_000) * float(preco_atual.preco_milhao_tokens_saida)
    custo_total = custo_entrada + custo_saida

    # 3. Salvar no banco
    db_custo = models.LLMCustoUso(
        **usage.model_dump(),
        timestamp_chamada=datetime.datetime.now(datetime.timezone.utc),
        custo_calculado=custo_total
    )
    db.add(db_custo)
    db.commit()
    db.refresh(db_custo)
    return db_custo

@router.get("/", response_model=List[schemas.LLMCustoUso], summary="Lista os registros de custo de LLM")
def read_llm_custos(
    projeto_id: Optional[int] = None, 
    db: Session = Depends(get_db), 
    user: models.Usuario = Depends(require_permission("llm_custo:ver"))
):
    query = db.query(models.LLMCustoUso)
    if projeto_id:
        query = query.filter(models.LLMCustoUso.projeto_id == projeto_id)
    return query.all()
