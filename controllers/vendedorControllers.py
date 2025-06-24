from fastapi import APIRouter, Body, HTTPException
from typing import List

from my_types import VendedorCadastroDTO, VendedorDTO, VendedorLoadedDTO
from services import VendedorCrud

router = APIRouter()
crud = VendedorCrud()

@router.post("/vendedores", response_model=VendedorDTO)
def create_vendedor(data: VendedorCadastroDTO):
    return crud.create(data)

@router.get("/vendedores/{id}", response_model=VendedorLoadedDTO)
def get_vendedor(id: str):
    vendedor = crud.read(id)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.patch("/vendedores/{id}", response_model=VendedorDTO)
def update_vendedor(id: str, novo_nome: str = Body(..., embed=True)):
    vendedor = crud.update(id, novo_nome)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.delete("/vendedores/{id}", status_code=204)
def delete_vendedor(id: str):
    crud.delete(id)
    return None

@router.get("/vendedores", response_model=List[VendedorDTO])
def list_vendedores():
    return crud.list_all()