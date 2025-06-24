from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class ProdutoCadastroDTO(BaseModel):
    id_vendedor: str
    nome: str
    descricao: Optional[str] = None
    preco: Optional[Decimal] = None
    estoque: int