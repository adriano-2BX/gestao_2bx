# app/api/endpoints/certificados_ssl.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.CertificadoSSL, status_code=201, summary="Adiciona um novo certificado SSL")
def create_certificado(
    certificado: schemas.CertificadoSSLCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("certificado_ssl:criar"))
):
    db_certificado = models.CertificadoSSL(**certificado.model_dump())
    db.add(db_certificado)
    db.commit()
    db.refresh(db_certificado)
    return db_certificado

@router.get("/", response_model=List[schemas.CertificadoSSL], summary="Lista todos os certificados SSL")
def read_certificados(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("certificado_ssl:ver"))
):
    certificados = db.query(models.CertificadoSSL).offset(skip).limit(limit).all()
    return certificados

@router.get("/{certificado_id}", response_model=schemas.CertificadoSSL, summary="Busca um certificado SSL específico")
def read_certificado(
    certificado_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("certificado_ssl:ver"))
):
    db_certificado = db.query(models.CertificadoSSL).filter(models.CertificadoSSL.id == certificado_id).first()
    if db_certificado is None:
        raise HTTPException(status_code=404, detail="Certificado SSL não encontrado")
    return db_certificado

@router.put("/{certificado_id}", response_model=schemas.CertificadoSSL, summary="Atualiza um certificado SSL")
def update_certificado(
    certificado_id: int, 
    certificado: schemas.CertificadoSSLUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("certificado_ssl:editar"))
):
    db_certificado = db.query(models.CertificadoSSL).filter(models.CertificadoSSL.id == certificado_id).first()
    if db_certificado is None:
        raise HTTPException(status_code=404, detail="Certificado SSL não encontrado")

    update_data = certificado.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_certificado, key, value)

    db.add(db_certificado)
    db.commit()
    db.refresh(db_certificado)
    return db_certificado

@router.delete("/{certificado_id}", status_code=204, summary="Deleta um certificado SSL")
def delete_certificado(
    certificado_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("certificado_ssl:deletar"))
):
    db_certificado = db.query(models.CertificadoSSL).filter(models.CertificadoSSL.id == certificado_id).first()
    if db_certificado is None:
        raise HTTPException(status_code=404, detail="Certificado SSL não encontrado")

    db.delete(db_certificado)
    db.commit()
    return
