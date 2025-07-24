# app/api/endpoints/credenciais.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission
from app.core.security import encrypt_data, decrypt_data

router = APIRouter()

@router.post("/", response_model=schemas.Credencial, status_code=201, summary="Cria uma nova credencial de forma segura")
def create_credencial(credencial: schemas.CredencialCreate, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("credencial:criar"))):
    encrypted_dados = encrypt_data(credencial.dados_credencial)
    encrypted_notas = encrypt_data({"notas": credencial.notas_seguras}) if credencial.notas_seguras else None
    
    db_credencial = models.Credencial(
        nome=credencial.nome,
        tipo_credencial=credencial.tipo_credencial,
        dados_credencial_encrypted=encrypted_dados,
        notas_seguras_encrypted=encrypted_notas
    )
    db.add(db_credencial)
    db.commit()
    db.refresh(db_credencial)
    return db_credencial

@router.get("/", response_model=List[schemas.Credencial], summary="Lista os metadados das credenciais")
def read_credenciais(db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("credencial:ver"))):
    return db.query(models.Credencial).all()

@router.get("/{credencial_id}/revelar", response_model=schemas.CredencialRevelada, summary="Revela o conteúdo de uma credencial")
def reveal_credencial(credencial_id: int, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("credencial:revelar"))):
    db_credencial = db.query(models.Credencial).filter(models.Credencial.id == credencial_id).first()
    if not db_credencial:
        raise HTTPException(status_code=404, detail="Credencial não encontrada")
    
    dados_revelados = decrypt_data(db_credencial.dados_credencial_encrypted)
    notas_reveladas = decrypt_data(db_credencial.notas_seguras_encrypted)["notas"] if db_credencial.notas_seguras_encrypted else None
    
    return schemas.CredencialRevelada(dados_credencial=dados_revelados, notas_seguras=notas_reveladas)

# Adicionar rotas de PUT e DELETE aqui, seguindo o mesmo padrão de segurança.
