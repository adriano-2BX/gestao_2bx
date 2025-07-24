from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.LLMModelo, status_code=201)
def create_llm_modelo(modelo: schemas.LLMModeloCreate, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("llm_modelo:criar"))):
    db_modelo = models.LLMModelo(**modelo.model_dump())
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

@router.get("/", response_model=List[schemas.LLMModelo])
def read_llm_modelos(db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("llm_modelo:ver"))):
    return db.query(models.LLMModelo).all()
