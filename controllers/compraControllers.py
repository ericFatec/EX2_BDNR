from fastapi import APIRouter, HTTPException
from typing import List

from my_types import CompraDTO, CompraCadastroDTO, CompraAtualizarDTO
from services import CompraCrud

router = APIRouter()
crud = CompraCrud()

@router.post("/compras", response_model=CompraDTO)
def create_compra(data: CompraCadastroDTO):
    return crud.create(data)

@router.get("/compras/{id}", response_model=CompraDTO)
def get_compra(id: str):
    compra = crud.read(id)
    if not compra:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    return compra

@router.patch("/compras/{id}", response_model=CompraDTO)
def update_compra(id: str, data: CompraAtualizarDTO):
    compra = crud.update(id, data)
    if not compra:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    return compra

@router.post("/compras/{id}/confirmar-pagamento", response_model=CompraDTO)
def confirm_payment(id: str):
    compra = crud.confirm_payment(id)
    if not compra:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    return compra

@router.delete("/compras/{id}", status_code=204)
def delete_compra(id: str):
    crud.delete(id)
    return None

@router.get("/compras", response_model=List[CompraDTO])
def list_compras():
    return crud.list_all()