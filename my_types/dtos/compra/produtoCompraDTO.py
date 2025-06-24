from pydantic import BaseModel
from decimal import Decimal

class ProdutoCompraDTO(BaseModel):
    id_produto: str
    nome_produto: str
    preco_unitario: Decimal
    quantidade: int