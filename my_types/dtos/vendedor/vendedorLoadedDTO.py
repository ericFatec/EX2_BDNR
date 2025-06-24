from pydantic import BaseModel, Field
from typing import List
from decimal import Decimal

from ..avaliacao.avaliacaoDTO import AvaliacaoDTO
from .vendaDTO import VendaDTO
from .produtoVendedor import ProdutoVendedor

class VendedorLoadedDTO(BaseModel):
    id: str = Field(alias="_id")
    id_usuario: str
    nome_usuario: str
    nome_loja: str
    total_avaliacao: Decimal
    avaliacoes: List[AvaliacaoDTO]
    vendas: List[VendaDTO]
    produtos: List[ProdutoVendedor]