# app/api/endpoints/servidores.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Servidor, status_code=201, summary="Cria um novo servidor")
def create_servidor(
    servidor: schemas.ServidorCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("servidor:criar"))
):
    db_servidor = models.Servidor(**servidor.model_dump())
    db.add(db_servidor)
    db.commit()
    db.refresh(db_servidor)
    return db_servidor

@router.get("/", response_model=List[schemas.Servidor], summary="Lista todos os servidores")
def read_servidores(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("servidor:ver"))
):
    servidores = db.query(models.Servidor).offset(skip).limit(limit).all()
    return servidores

@router.get("/{servidor_id}", response_model=schemas.Servidor, summary="Busca um servidor específico")
def read_servidor(
    servidor_id: int, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("servidor:ver"))
):
    db_servidor = db.query(models.Servidor).filter(models.Servidor.id == servidor_id).first()
    if db_servidor is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")
    return db_servidor

@router.put("/{servidor_id}", response_model=schemas.Servidor, summary="Atualiza um servidor")
def update_servidor(
    servidor_id: int, 
    servidor: schemas.ServidorUpdate, 
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("servidor:editar"))
):
    db_servidor = db.query(models.Servidor).filter(models.Servidor.id == servidor_id).first()
    if db_servidor is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")

    update_data = servidor.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_servidor, key, value)

    db.add(db_servidor)
    db.commit()
    db.refresh(db_servidor)
    return db_servidor

@router.delete("/{servidor_id}", status_code=204, summary="Deleta um servidor")
def delete_servidor(
    servidor_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("servidor:deletar"))
):
    db_servidor = db.query(models.Servidor).filter(models.Servidor.id == servidor_id).first()
    if db_servidor is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")

    db.delete(db_servidor)
    db.commit()
    return
