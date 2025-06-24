from pydantic import BaseModel
from .enderecoDTO import EnderecoDTO
from typing import Optional

class UsuarioAtualizarDTO(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    endereco: Optional[EnderecoDTO] = None