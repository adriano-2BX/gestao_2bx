# app/api/endpoints/fluxos_automacao.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.FluxoAutomacao, status_code=201, summary="Cria um novo fluxo de automação")
def create_fluxo(
    fluxo: schemas.FluxoAutomacaoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("fluxo_automacao:criar"))
):
    db_fluxo = models.FluxoAutomacao(**fluxo.model_dump())
    db.add(db_fluxo)
    db.commit()
    db.refresh(db_fluxo)
    return db_fluxo

@router.get("/", response_model=List[schemas.FluxoAutomacao], summary="Lista todos os fluxos de automação")
def read_fluxos(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("fluxo_automacao:ver"))
):
    fluxos = db.query(models.FluxoAutomacao).offset(skip).limit(limit).all()
    return fluxos

@router.get("/{fluxo_id}", response_model=schemas.FluxoAutomacao, summary="Busca um fluxo de automação específico")
def read_fluxo(
    fluxo_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("fluxo_automacao:ver"))
):
    db_fluxo = db.query(models.FluxoAutomacao).filter(models.FluxoAutomacao.id == fluxo_id).first()
    if db_fluxo is None:
        raise HTTPException(status_code=404, detail="Fluxo de automação não encontrado")
    return db_fluxo

@router.put("/{fluxo_id}", response_model=schemas.FluxoAutomacao, summary="Atualiza um fluxo de automação")
def update_fluxo(
    fluxo_id: int, 
    fluxo: schemas.FluxoAutomacaoUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("fluxo_automacao:editar"))
):
    db_fluxo = db.query(models.FluxoAutomacao).filter(models.FluxoAutomacao.id == fluxo_id).first()
    if db_fluxo is None:
        raise HTTPException(status_code=404, detail="Fluxo de automação não encontrado")

    update_data = fluxo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_fluxo, key, value)

    db.add(db_fluxo)
    db.commit()
    db.refresh(db_fluxo)
    return db_fluxo

@router.delete("/{fluxo_id}", status_code=204, summary="Deleta um fluxo de automação")
def delete_fluxo(
    fluxo_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("fluxo_automacao:deletar"))
):
    db_fluxo = db.query(models.FluxoAutomacao).filter(models.FluxoAutomacao.id == fluxo_id).first()
    if db_fluxo is None:
        raise HTTPException(status_code=404, detail="Fluxo de automação não encontrado")

    db.delete(db_fluxo)
    db.commit()
    return
