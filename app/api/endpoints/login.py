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
    user = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()
    
    if not user or not security.verify_password(form_data.password, user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- ROTA DE DEPURAÇÃO TEMPORÁRIA ---
@router.get("/gerar-hash/{senha}", tags=["Debug"])
def gerar_hash_senha(senha: str):
    """
    Endpoint temporário para gerar um hash de senha válido.
    Use-o para obter o hash correto e depois remova este endpoint.
    """
    hash_gerado = security.get_password_hash(senha)
    print("==================================================")
    print(f"HASH GERADO PARA A SENHA '{senha}':")
    print(hash_gerado)
    print("==================================================")
    return {"senha_original": senha, "hash_gerado": hash_gerado}
