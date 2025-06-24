from pydantic import BaseModel, Field
from typing import List, Optional

from .enderecoDTO import EnderecoDTO
from .perfilVendedor import PerfilVendedor
from ...enums.tipoUsuario import TipoUsuario

class UsuarioDTO(BaseModel):
    id: str = Field(alias="_id")
    nome: str
    email: str
    endereco: EnderecoDTO
    tipos: List[TipoUsuario]
    compras: int
    avaliacoes: int
    perfil_vendedor: Optional[PerfilVendedor]