# app/api/deps.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session, joinedload
from jose import JWTError, jwt

from app import models, schemas
from app.core.db import get_db
from app.core.config import settings

# Atualizamos a tokenUrl para o caminho completo e correto, que a documentação usará.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.Usuario).options(
        joinedload(models.Usuario.papel).joinedload(models.Papel.permissoes)
    ).filter(models.Usuario.email == token_data.email).first()

    if user is None:
        raise credentials_exception
    return user

def require_permission(permission_name: str):
    """
    Cria uma dependência que verifica se o usuário logado tem uma permissão específica.
    """
    def dependency(current_user: models.Usuario = Depends(get_current_user)) -> models.Usuario:
        if not current_user.papel:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuário não possui um papel definido."
            )
        
        user_permissions = {p.nome for p in current_user.papel.permissoes}
        
        if permission_name not in user_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="O usuário não tem permissão para executar esta ação."
            )
        return current_user
    
    return dependency
