from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class ProdutoAtualizarDTO(BaseModel):
    nome: Optional[str]
    descricao: Optional[str] = None
    preco: Optional[Decimal]
    estoque: Optional[int]