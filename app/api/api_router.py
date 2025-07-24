# app/api/api_router.py
from fastapi import APIRouter
from .endpoints import clientes

api_router = APIRouter()
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
