from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class ProdutoDTO(BaseModel):
    id: str = Field(alias="_id")
    id_vendedor: str
    nome_loja: str
    nome: str
    descricao: Optional[str]
    preco: Decimal
    estoque: int
    total_avaliacao: Decimal
    avaliacoes: int