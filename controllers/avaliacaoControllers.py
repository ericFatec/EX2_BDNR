from fastapi import APIRouter, HTTPException
from typing import List

from my_types import (
    AvaliacaoDTO,
    AvaliacaoCadastroDTO,
    AvaliacaoAtualizarDTO,
)
from services import AvalCrud

router = APIRouter()
crud = AvalCrud()

@router.post("/avaliacoes", response_model=AvaliacaoDTO)
def create_avaliacao(data: AvaliacaoCadastroDTO):
    return crud.create(data)

@router.get("/avaliacoes/{id}", response_model=AvaliacaoDTO)
def get_avaliacao(id: str):
    avaliacao = crud.read(id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao

@router.patch("/avaliacoes/{id}", response_model=AvaliacaoDTO)
def update_avaliacao(id: str, data: AvaliacaoAtualizarDTO):
    avaliacao = crud.update(id, data)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao

@router.delete("/avaliacoes/{id}", status_code=204)
def delete_avaliacao(id: str):
    crud.delete(id)
    return None

@router.get("/avaliacoes", response_model=List[AvaliacaoDTO])
def list_avaliacoes():
    return crud.list_all()
