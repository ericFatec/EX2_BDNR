from pydantic import BaseModel, Field
from decimal import Decimal

class ProdutoVendedor(BaseModel):
    id: str = Field(alias="_id")
    nome: str
    descricao: str
    preco: Decimal
    estoque: int
    total_avaliacao: Decimal