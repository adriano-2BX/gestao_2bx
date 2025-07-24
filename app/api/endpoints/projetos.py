# app/api/endpoints/projetos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Projeto, status_code=201, summary="Cria um novo projeto")
def create_projeto(projeto: schemas.ProjetoCreate, db: Session = Depends(get_db)):
    db_projeto = models.projeto.Projeto(**projeto.model_dump())
    db.add(db_projeto)
    db.commit()
    db.refresh(db_projeto)
    return db_projeto

@router.get("/", response_model=List[schemas.Projeto], summary="Lista todos os projetos")
def read_projetos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projetos = db.query(models.projeto.Projeto).offset(skip).limit(limit).all()
    return projetos
