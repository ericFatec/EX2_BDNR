from pydantic import BaseModel
from .enderecoDTO import EnderecoDTO
from ...enums.tipoUsuario import TipoUsuario
from typing import List, Optional

class UsuarioCadastroDTO(BaseModel):
    nome: str
    email: str
    senha: str
    endereco: EnderecoDTO
    tipos: List[TipoUsuario]
    nome_loja: Optional[str] = None