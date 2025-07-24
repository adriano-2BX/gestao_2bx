from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission
import datetime

router = APIRouter()

@router.get("/", response_model=List[schemas.Fatura])
def read_faturas(cliente_id: Optional[int] = None, status: Optional[str] = None, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("fatura:ver"))):
    query = db.query(models.Fatura)
    if cliente_id:
        query = query.filter(models.Fatura.cliente_id == cliente_id)
    if status:
        query = query.filter(models.Fatura.status == status)
    return query.all()

@router.post("/{fatura_id}/marcar-paga", response_model=schemas.Fatura)
def mark_fatura_as_paid(fatura_id: int, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("fatura:editar"))):
    db_fatura = db.query(models.Fatura).filter(models.Fatura.id == fatura_id).first()
    if not db_fatura:
        raise HTTPException(status_code=404, detail="Fatura não encontrada")
    db_fatura.status = 'PAGA'
    db_fatura.data_pagamento = datetime.date.today()
    db.commit()
    db.refresh(db_fatura)
    return db_fatura
