# app/api/endpoints/clientes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .... import models, schemas # Usamos .... para subir 4 níveis na estrutura de pastas
from ....core.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Cliente, status_code=201, summary="Cria um novo cliente")
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    """
    Cria um novo cliente no banco de dados.
    """
    db_cliente = models.cliente.Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@router.get("/", response_model=List[schemas.Cliente], summary="Lista todos os clientes")
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna uma lista de clientes com paginação.
    """
    clientes = db.query(models.cliente.Cliente).offset(skip).limit(limit).all()
    return clientes
