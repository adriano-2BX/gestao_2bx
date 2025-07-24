# app/api/endpoints/dominios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Dominio, status_code=201, summary="Registra um novo domínio")
def create_dominio(
    dominio: schemas.DominioCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("dominio:criar"))
):
    db_dominio = models.Dominio(**dominio.model_dump())
    db.add(db_dominio)
    db.commit()
    db.refresh(db_dominio)
    return db_dominio

@router.get("/", response_model=List[schemas.Dominio], summary="Lista todos os domínios")
def read_dominios(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("dominio:ver"))
):
    dominios = db.query(models.Dominio).offset(skip).limit(limit).all()
    return dominios

@router.get("/{dominio_id}", response_model=schemas.Dominio, summary="Busca um domínio específico")
def read_dominio(
    dominio_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("dominio:ver"))
):
    db_dominio = db.query(models.Dominio).filter(models.Dominio.id == dominio_id).first()
    if db_dominio is None:
        raise HTTPException(status_code=404, detail="Domínio não encontrado")
    return db_dominio

@router.put("/{dominio_id}", response_model=schemas.Dominio, summary="Atualiza um domínio")
def update_dominio(
    dominio_id: int, 
    dominio: schemas.DominioUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("dominio:editar"))
):
    db_dominio = db.query(models.Dominio).filter(models.Dominio.id == dominio_id).first()
    if db_dominio is None:
        raise HTTPException(status_code=404, detail="Domínio não encontrado")

    update_data = dominio.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_dominio, key, value)

    db.add(db_dominio)
    db.commit()
    db.refresh(db_dominio)
    return db_dominio

@router.delete("/{dominio_id}", status_code=204, summary="Deleta um domínio")
def delete_dominio(
    dominio_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("dominio:deletar"))
):
    db_dominio = db.query(models.Dominio).filter(models.Dominio.id == dominio_id).first()
    if db_dominio is None:
        raise HTTPException(status_code=404, detail="Domínio não encontrado")

    db.delete(db_dominio)
    db.commit()
    return
