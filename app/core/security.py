# app/core/security.py
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from cryptography.fernet import Fernet
import json
from .config import settings

# --- LÓGICA DE CRIPTOGRAFIA ---
fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_data(data: dict) -> str:
    """Criptografa um dicionário (JSON) e retorna uma string segura."""
    if not isinstance(data, dict):
        raise TypeError("Apenas dicionários podem ser criptografados")
    json_data = json.dumps(data)
    encrypted_data = fernet.encrypt(json_data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str) -> dict:
    """Descriptografa dados e retorna o dicionário (JSON) original."""
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return json.loads(decrypted_data.decode())

# --- LÓGICA DE SENHAS ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto plano corresponde à senha com hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Gera o hash de uma senha em texto plano."""
    return pwd_context.hash(password)

# --- LÓGICA DE TOKEN JWT ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
