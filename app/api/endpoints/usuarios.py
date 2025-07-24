# app/api/endpoints/usuarios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/", response_model=schemas.Usuario, status_code=201, summary="Cria um novo usuário")
def create_user(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.Usuario).filter(models.Usuario.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já registrado")

    hashed_password = get_password_hash(user.password)
    db_user = models.Usuario(
        email=user.email,
        nome=user.nome,
        senha_hash=hashed_password,
        cargo=user.cargo,
        papel_id=user.papel_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[schemas.Usuario], summary="Lista todos os usuários")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.Usuario).offset(skip).limit(limit).all()
    return users
