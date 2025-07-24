# app/api/endpoints/tarefas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas
from app.core.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Tarefa, status_code=201, summary="Cria uma nova tarefa")
def create_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    # Opcional: Verificar se o projeto existe antes de criar a tarefa
    db_projeto = db.query(models.Projeto).filter(models.Projeto.id == tarefa.projeto_id).first()
    if not db_projeto:
        raise HTTPException(status_code=404, detail=f"Projeto com id {tarefa.projeto_id} não encontrado")

    db_tarefa = models.Tarefa(**tarefa.model_dump())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

@router.get("/", response_model=List[schemas.Tarefa], summary="Lista tarefas")
def read_tarefas(projeto_id: Optional[int] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lista todas as tarefas. 
    - Use o parâmetro `projeto_id` para filtrar tarefas de um projeto específico.
    """
    query = db.query(models.Tarefa)
    if projeto_id:
        query = query.filter(models.Tarefa.projeto_id == projeto_id)

    tarefas = query.offset(skip).limit(limit).all()
    return tarefas

@router.get("/{tarefa_id}", response_model=schemas.Tarefa, summary="Busca uma tarefa específica")
def read_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if db_tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_tarefa

@router.put("/{tarefa_id}", response_model=schemas.Tarefa, summary="Atualiza uma tarefa")
def update_tarefa(tarefa_id: int, tarefa: schemas.TarefaUpdate, db: Session = Depends(get_db)):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if db_tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    update_data = tarefa.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_tarefa, key, value)

    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa
