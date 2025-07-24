from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.CatalogoServico, status_code=201)
def create_servico(servico: schemas.CatalogoServicoCreate, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("catalogo_servico:criar"))):
    db_servico = models.CatalogoServico(**servico.model_dump())
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico

@router.get("/", response_model=List[schemas.CatalogoServico])
def read_servicos(db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("catalogo_servico:ver"))):
    return db.query(models.CatalogoServico).all()
