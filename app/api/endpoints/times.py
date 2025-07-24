# app/api/endpoints/times.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Time, status_code=201, summary="Cria um novo time")
def create_time(time: schemas.TimeCreate, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("time:criar"))):
    db_time = models.Time(**time.model_dump())
    db.add(db_time)
    db.commit()
    db.refresh(db_time)
    return db_time

@router.get("/", response_model=List[schemas.Time], summary="Lista todos os times")
def read_times(db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("time:ver"))):
    return db.query(models.Time).options(joinedload(models.Time.usuarios)).all()

@router.post("/{time_id}/membros", response_model=schemas.Time, summary="Adiciona um membro a um time")
def add_membro_to_time(time_id: int, link: schemas.LinkUsuarioToTime, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("time:editar_membros"))):
    db_time = db.query(models.Time).options(joinedload(models.Time.usuarios)).filter(models.Time.id == time_id).first()
    if not db_time:
        raise HTTPException(status_code=404, detail="Time não encontrado")

    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == link.usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if db_usuario not in db_time.usuarios:
        db_time.usuarios.append(db_usuario)
        db.commit()
        db.refresh(db_time)

    return db_time

@router.delete("/{time_id}/membros/{usuario_id}", response_model=schemas.Time, summary="Remove um membro de um time")
def remove_membro_from_time(time_id: int, usuario_id: int, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("time:editar_membros"))):
    db_time = db.query(models.Time).options(joinedload(models.Time.usuarios)).filter(models.Time.id == time_id).first()
    if not db_time:
        raise HTTPException(status_code=404, detail="Time não encontrado")

    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if db_usuario in db_time.usuarios:
        db_time.usuarios.remove(db_usuario)
        db.commit()
        db.refresh(db_time)

    return db_time
