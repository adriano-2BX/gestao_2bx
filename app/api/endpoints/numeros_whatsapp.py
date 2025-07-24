# app/api/endpoints/numeros_whatsapp.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.NumeroWhatsApp, status_code=201, summary="Adiciona um novo número de WhatsApp")
def create_numero(
    numero: schemas.NumeroWhatsAppCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("numero_whatsapp:criar"))
):
    db_numero = models.NumeroWhatsApp(**numero.model_dump())
    db.add(db_numero)
    db.commit()
    db.refresh(db_numero)
    return db_numero

@router.get("/", response_model=List[schemas.NumeroWhatsApp], summary="Lista todos os números de WhatsApp")
def read_numeros(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("numero_whatsapp:ver"))
):
    numeros = db.query(models.NumeroWhatsApp).offset(skip).limit(limit).all()
    return numeros

@router.get("/{numero_id}", response_model=schemas.NumeroWhatsApp, summary="Busca um número de WhatsApp específico")
def read_numero(
    numero_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("numero_whatsapp:ver"))
):
    db_numero = db.query(models.NumeroWhatsApp).filter(models.NumeroWhatsApp.id == numero_id).first()
    if db_numero is None:
        raise HTTPException(status_code=404, detail="Número de WhatsApp não encontrado")
    return db_numero

@router.put("/{numero_id}", response_model=schemas.NumeroWhatsApp, summary="Atualiza um número de WhatsApp")
def update_numero(
    numero_id: int, 
    numero: schemas.NumeroWhatsAppUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("numero_whatsapp:editar"))
):
    db_numero = db.query(models.NumeroWhatsApp).filter(models.NumeroWhatsApp.id == numero_id).first()
    if db_numero is None:
        raise HTTPException(status_code=404, detail="Número de WhatsApp não encontrado")

    update_data = numero.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_numero, key, value)

    db.add(db_numero)
    db.commit()
    db.refresh(db_numero)
    return db_numero

@router.delete("/{numero_id}", status_code=204, summary="Deleta um número de WhatsApp")
def delete_numero(
    numero_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("numero_whatsapp:deletar"))
):
    db_numero = db.query(models.NumeroWhatsApp).filter(models.NumeroWhatsApp.id == numero_id).first()
    if db_numero is None:
        raise HTTPException(status_code=404, detail="Número de WhatsApp não encontrado")

    db.delete(db_numero)
    db.commit()
    return
