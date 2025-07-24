# app/api/endpoints/conexoes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List

from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Conexao, status_code=201, summary="Cria uma nova conexão entre duas entidades")
def create_conexao(
    conexao: schemas.ConexaoCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("conexao:criar"))
):
    # Opcional: Adicionar validação para ver se as entidades de origem/destino existem
    db_conexao = models.Conexao(**conexao.model_dump())
    db.add(db_conexao)
    db.commit()
    db.refresh(db_conexao)
    return db_conexao

@router.get("/entidade/{tabela}/{id}", response_model=List[schemas.Conexao], summary="Lista todas as conexões de uma entidade específica")
def read_conexoes_for_entidade(
    tabela: str,
    id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("conexao:ver"))
):
    """
    Busca todas as conexões onde a entidade especificada é a origem OU o destino.
    Esta é a rota chave para construir os grafos de dependência.
    """
    conexoes = db.query(models.Conexao).filter(
        or_(
            (models.Conexao.origem_tabela == tabela) & (models.Conexao.origem_id == id),
            (models.Conexao.destino_tabela == tabela) & (models.Conexao.destino_id == id)
        )
    ).all()
    return conexoes

@router.delete("/{conexao_id}", status_code=204, summary="Deleta uma conexão")
def delete_conexao(
    conexao_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(require_permission("conexao:deletar"))
):
    db_conexao = db.query(models.Conexao).filter(models.Conexao.id == conexao_id).first()
    if db_conexao is None:
        raise HTTPException(status_code=404, detail="Conexão não encontrada")

    db.delete(db_conexao)
    db.commit()
    return
