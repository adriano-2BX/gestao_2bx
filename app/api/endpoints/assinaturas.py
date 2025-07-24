from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Assinatura, status_code=201)
def create_assinatura(assinatura: schemas.AssinaturaCreate, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("assinatura:criar"))):
    db_assinatura = models.Assinatura(**assinatura.model_dump())
    db.add(db_assinatura)
    db.commit()
    db.refresh(db_assinatura)
    return db_assinatura

@router.get("/cliente/{cliente_id}", response_model=List[schemas.Assinatura])
def read_assinaturas_by_cliente(cliente_id: int, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("assinatura:ver"))):
    return db.query(models.Assinatura).filter(models.Assinatura.cliente_id == cliente_id).all()
