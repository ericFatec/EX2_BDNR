from pydantic import BaseModel, Field
from typing import List, Optional

from .enderecoDTO import EnderecoDTO
from .favorito import Favorito
from ..compra.compraDTO import CompraDTO
from .avaliacaoUsuario import AvaliacaoUsuario
from .perfilVendedor import PerfilVendedor
from ...enums.tipoUsuario import TipoUsuario

class UsuarioLoadedDTO(BaseModel):
    id: str = Field(alias="_id")
    nome: str
    email: str
    senha: str
    endereco: EnderecoDTO
    tipos: List[TipoUsuario]
    favoritos: List[Favorito]
    compras: List[CompraDTO]
    avaliacoes: List[AvaliacaoUsuario]
    perfil_vendedor: Optional[PerfilVendedor]