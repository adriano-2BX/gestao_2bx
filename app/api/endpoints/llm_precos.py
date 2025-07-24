from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.LLMPreco, status_code=201)
def create_llm_preco(preco: schemas.LLMPrecoCreate, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("llm_preco:criar"))):
    db_preco = models.LLMPreco(**preco.model_dump())
    db.add(db_preco)
    db.commit()
    db.refresh(db_preco)
    return db_preco

@router.get("/modelo/{modelo_id}", response_model=List[schemas.LLMPreco])
def read_precos_by_modelo(modelo_id: int, db: Session = Depends(get_db), user: models.Usuario = Depends(require_permission("llm_preco:ver"))):
    return db.query(models.LLMPreco).filter(models.LLMPreco.modelo_id == modelo_id).all()
