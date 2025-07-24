# app/api/endpoints/aplicacoes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Aplicacao, status_code=201, summary="Cria uma nova aplicação")
def create_aplicacao(
    aplicacao: schemas.AplicacaoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("aplicacao:criar"))
):
    db_aplicacao = models.Aplicacao(**aplicacao.model_dump())
    db.add(db_aplicacao)
    db.commit()
    db.refresh(db_aplicacao)
    return db_aplicacao

@router.get("/", response_model=List[schemas.Aplicacao], summary="Lista todas as aplicações")
def read_aplicacoes(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("aplicacao:ver"))
):
    aplicacoes = db.query(models.Aplicacao).offset(skip).limit(limit).all()
    return aplicacoes

@router.get("/{aplicacao_id}", response_model=schemas.Aplicacao, summary="Busca uma aplicação específica")
def read_aplicacao(
    aplicacao_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("aplicacao:ver"))
):
    db_aplicacao = db.query(models.Aplicacao).filter(models.Aplicacao.id == aplicacao_id).first()
    if db_aplicacao is None:
        raise HTTPException(status_code=404, detail="Aplicação não encontrada")
    return db_aplicacao

@router.put("/{aplicacao_id}", response_model=schemas.Aplicacao, summary="Atualiza uma aplicação")
def update_aplicacao(
    aplicacao_id: int, 
    aplicacao: schemas.AplicacaoUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("aplicacao:editar"))
):
    db_aplicacao = db.query(models.Aplicacao).filter(models.Aplicacao.id == aplicacao_id).first()
    if db_aplicacao is None:
        raise HTTPException(status_code=404, detail="Aplicação não encontrada")

    update_data = aplicacao.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_aplicacao, key, value)

    db.add(db_aplicacao)
    db.commit()
    db.refresh(db_aplicacao)
    return db_aplicacao

@router.delete("/{aplicacao_id}", status_code=204, summary="Deleta uma aplicação")
def delete_aplicacao(
    aplicacao_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("aplicacao:deletar"))
):
    db_aplicacao = db.query(models.Aplicacao).filter(models.Aplicacao.id == aplicacao_id).first()
    if db_aplicacao is None:
        raise HTTPException(status_code=404, detail="Aplicação não encontrada")

    db.delete(db_aplicacao)
    db.commit()
    return
