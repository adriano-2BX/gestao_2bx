# app/api/endpoints/permissoes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.get("/", response_model=List[schemas.Permissao], summary="Lista todas as permissões")
def read_permissoes(db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("permissao:ver"))):
    return db.query(models.Permissao).all()
