# app/api/endpoints/instancias_api_whatsapp.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.InstanciaAPIWhatsApp, status_code=201, summary="Cria uma nova instância de API do WhatsApp")
def create_instancia(
    instancia: schemas.InstanciaAPIWhatsAppCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("instancia_api_whatsapp:criar"))
):
    db_instancia = models.InstanciaAPIWhatsApp(**instancia.model_dump())
    db.add(db_instancia)
    db.commit()
    db.refresh(db_instancia)
    return db_instancia

@router.get("/", response_model=List[schemas.InstanciaAPIWhatsApp], summary="Lista todas as instâncias")
def read_instancias(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("instancia_api_whatsapp:ver"))
):
    instancias = db.query(models.InstanciaAPIWhatsApp).offset(skip).limit(limit).all()
    return instancias

@router.get("/{instancia_id}", response_model=schemas.InstanciaAPIWhatsApp, summary="Busca uma instância específica")
def read_instancia(
    instancia_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("instancia_api_whatsapp:ver"))
):
    db_instancia = db.query(models.InstanciaAPIWhatsApp).filter(models.InstanciaAPIWhatsApp.id == instancia_id).first()
    if db_instancia is None:
        raise HTTPException(status_code=404, detail="Instância não encontrada")
    return db_instancia

@router.put("/{instancia_id}", response_model=schemas.InstanciaAPIWhatsApp, summary="Atualiza uma instância")
def update_instancia(
    instancia_id: int, 
    instancia: schemas.InstanciaAPIWhatsAppUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("instancia_api_whatsapp:editar"))
):
    db_instancia = db.query(models.InstanciaAPIWhatsApp).filter(models.InstanciaAPIWhatsApp.id == instancia_id).first()
    if db_instancia is None:
        raise HTTPException(status_code=404, detail="Instância não encontrada")

    update_data = instancia.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_instancia, key, value)

    db.add(db_instancia)
    db.commit()
    db.refresh(db_instancia)
    return db_instancia

@router.delete("/{instancia_id}", status_code=204, summary="Deleta uma instância")
def delete_instancia(
    instancia_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("instancia_api_whatsapp:deletar"))
):
    db_instancia = db.query(models.InstanciaAPIWhatsApp).filter(models.InstanciaAPIWhatsApp.id == instancia_id).first()
    if db_instancia is None:
        raise HTTPException(status_code=404, detail="Instância não encontrada")

    db.delete(db_instancia)
    db.commit()
    return
