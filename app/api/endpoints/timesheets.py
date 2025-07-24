# app/api/endpoints/timesheets.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime

from app import models, schemas
from app.core.db import get_db
from app.api.deps import get_current_user, require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Timesheet, status_code=201, summary="Registra um novo apontamento de horas para o usuário logado")
def create_timesheet(
    timesheet: schemas.TimesheetCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user) # Apenas um usuário logado pode apontar horas
):
    # O usuario_id é pego do token, não do corpo da requisição, por segurança
    db_timesheet = models.Timesheet(**timesheet.model_dump(), usuario_id=current_user.id)
    db.add(db_timesheet)
    db.commit()
    db.refresh(db_timesheet)
    return db_timesheet

@router.get("/", response_model=List[schemas.Timesheet], summary="Lista apontamentos de horas")
def read_timesheets(
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("timesheet:ver_todos")), # Requer permissão especial para ver tudo
    usuario_id: Optional[int] = None, # Filtro opcional
    data_inicio: Optional[datetime.date] = None,
    data_fim: Optional[datetime.date] = None,
    skip: int = 0,
    limit: int = 100
):
    """
    Lista todos os apontamentos de horas. Requer permissão `timesheet:ver_todos`.
    Pode ser filtrado por `usuario_id` e por um intervalo de datas.
    """
    query = db.query(models.Timesheet)
    if usuario_id:
        query = query.filter(models.Timesheet.usuario_id == usuario_id)
    if data_inicio:
        query = query.filter(models.Timesheet.data >= data_inicio)
    if data_fim:
        query = query.filter(models.Timesheet.data <= data_fim)

    timesheets = query.order_by(models.Timesheet.data.desc()).offset(skip).limit(limit).all()
    return timesheets

@router.get("/me", response_model=List[schemas.Timesheet], summary="Lista meus próprios apontamentos de horas")
def read_my_timesheets(
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user), # Apenas o usuário logado
    skip: int = 0,
    limit: int = 100
):
    timesheets = db.query(models.Timesheet).filter(models.Timesheet.usuario_id == current_user.id).order_by(models.Timesheet.data.desc()).offset(skip).limit(limit).all()
    return timesheets
