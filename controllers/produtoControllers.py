from fastapi import APIRouter, HTTPException
from typing import List

from my_types import ProdutoCadastroDTO, ProdutoAtualizarDTO, ProdutoDTO, ProdutoLoadedDTO
from services import ProdutoCrud

router = APIRouter()
crud = ProdutoCrud()

@router.post("/produtos", response_model=ProdutoDTO)
def create_produto(data: ProdutoCadastroDTO):
    return crud.create(data)

@router.get("/produtos/{id}", response_model=ProdutoLoadedDTO)
def get_produto(id: str):
    produto = crud.read(id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.patch("/produtos/{id}", response_model=ProdutoDTO)
def update_produto(id: str, data: ProdutoAtualizarDTO):
    produto = crud.update(id, data)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/produtos/{id}", status_code=204)
def delete_produto(id: str):
    crud.delete(id)
    return None

@router.get("/produtos", response_model=List[ProdutoDTO])
def list_produtos():
    return crud.list_all()