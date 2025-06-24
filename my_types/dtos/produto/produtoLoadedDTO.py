from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional

from ..avaliacao.avaliacaoDTO import AvaliacaoDTO

class ProdutoLoadedDTO(BaseModel):
    id: str = Field(alias="_id")
    id_vendedor: str
    nome_loja: str
    nome: str
    descricao: Optional[str]
    preco: Decimal
    estoque: int
    total_avaliacao: Decimal
    avaliacoes: List[AvaliacaoDTO]