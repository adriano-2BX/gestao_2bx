# app/api/endpoints/papeis.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from app import models, schemas
from app.core.db import get_db
from app.api.deps import require_permission

router = APIRouter()

@router.post("/", response_model=schemas.Papel, status_code=201, summary="Cria um novo papel")
def create_papel(papel: schemas.PapelCreate, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("papel:criar"))):
    db_papel = models.Papel(**papel.model_dump())
    db.add(db_papel)
    db.commit()
    db.refresh(db_papel)
    return db_papel

@router.get("/", response_model=List[schemas.Papel], summary="Lista todos os papéis")
def read_papeis(db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("papel:ver"))):
    return db.query(models.Papel).options(joinedload(models.Papel.permissoes)).all()

@router.post("/{papel_id}/permissoes", response_model=schemas.Papel, summary="Associa uma permissão a um papel")
def link_permissao_to_papel(papel_id: int, link: schemas.LinkPermissaoToPapel, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("papel:editar_permissoes"))):
    db_papel = db.query(models.Papel).options(joinedload(models.Papel.permissoes)).filter(models.Papel.id == papel_id).first()
    if not db_papel:
        raise HTTPException(status_code=404, detail="Papel não encontrado")

    db_permissao = db.query(models.Permissao).filter(models.Permissao.id == link.permissao_id).first()
    if not db_permissao:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")

    if db_permissao not in db_papel.permissoes:
        db_papel.permissoes.append(db_permissao)
        db.commit()
        db.refresh(db_papel)

    return db_papel

@router.delete("/{papel_id}/permissoes/{permissao_id}", response_model=schemas.Papel, summary="Desassocia uma permissão de um papel")
def unlink_permissao_from_papel(papel_id: int, permissao_id: int, db: Session = Depends(get_db), current_user: models.Usuario = Depends(require_permission("papel:editar_permissoes"))):
    db_papel = db.query(models.Papel).options(joinedload(models.Papel.permissoes)).filter(models.Papel.id == papel_id).first()
    if not db_papel:
        raise HTTPException(status_code=404, detail="Papel não encontrado")

    db_permissao = db.query(models.Permissao).filter(models.Permissao.id == permissao_id).first()
    if not db_permissao:
        raise HTTPException(status_code=404, detail="Permissão não encontrada")

    if db_permissao in db_papel.permissoes:
        db_papel.permissoes.remove(db_permissao)
        db.commit()
        db.refresh(db_papel)

    return db_papel
