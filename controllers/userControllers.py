from fastapi import APIRouter, Body, HTTPException
from typing import List

from my_types import UsuarioCadastroDTO, UsuarioAtualizarDTO, UsuarioDTO, UsuarioLoadedDTO
from services import UsuarioCrud

router = APIRouter()
crud = UsuarioCrud()

@router.post("/usuarios", response_model=UsuarioDTO)
def create_usuario(data: UsuarioCadastroDTO):
    return crud.create(data)

@router.get("/usuarios/{id}", response_model=UsuarioLoadedDTO)
def get_usuario(id: str):
    usuario = crud.read(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.patch("/usuarios/{id}", response_model=UsuarioDTO)
def update_usuario(id: str, data: UsuarioAtualizarDTO):
    usuario = crud.update(id, data)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.patch("/usuarios/{id}/favoritar", status_code=204)
def update_usuario(id: str, id_produto: str = Body(..., embed=True)):
    crud.favoritar(id, id_produto)
    return "Produto adicionado aos favoritos."

@router.delete("/usuarios/{id}", status_code=204)
def delete_usuario(id: str):
    crud.delete(id)
    return None

@router.get("/usuarios", response_model=List[UsuarioDTO])
def list_usuarios():
    return crud.list_all()