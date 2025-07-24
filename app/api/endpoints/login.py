# app/api/endpoints/login.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app import models, schemas
from app.core.db import get_db
from app.core import security
from app.core.config import settings

router = APIRouter()

@router.post("/access-token", response_model=schemas.Token)
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    # --- INÍCIO DO CÓDIGO DE DEPURAÇÃO ---
    print("================ INICIANDO DEBUG DE LOGIN ================")
    print(f"Tentativa de login para o usuário: '{form_data.username}'")
    print(f"Senha recebida: '{form_data.password}'")
    # --- FIM DO CÓDIGO DE DEPURAÇÃO ---

    user = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()

    # --- INÍCIO DO CÓDIGO DE DEPURAÇÃO ---
    if not user:
        print("[DEBUG] Usuário NÃO encontrado no banco de dados.")
        print("================ FIM DO DEBUG DE LOGIN ================")
    else:
        print(f"[DEBUG] Usuário encontrado: ID {user.id}, Email {user.email}")
        print(f"[DEBUG] Hash da senha no banco: '{user.senha_hash}'")
    # --- FIM DO CÓDIGO DE DEPURAÇÃO ---

    if not user or not security.verify_password(form_data.password, user.senha_hash):
        # --- INÍCIO DO CÓDIGO DE DEPURAÇÃO ---
        if user:
             print("[DEBUG] A verificação da senha FALHOU.")
        print("================ FIM DO DEBUG DE LOGIN ================")
        # --- FIM DO CÓDIGO DE DEPURAÇÃO ---
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # --- INÍCIO DO CÓDIGO DE DEPURAÇÃO ---
    print("[DEBUG] A verificação da senha foi BEM-SUCEDIDA.")
    print("================ FIM DO DEBUG DE LOGIN ================")
    # --- FIM DO CÓDIGO DE DEPURAÇÃO ---

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}OKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
