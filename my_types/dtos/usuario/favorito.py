from pydantic import BaseModel, Field
from decimal import Decimal

class Favorito(BaseModel):
    id: str = Field(alias="_id")
    nome: str
    preco: Decimal
    estoque: int
    total_avaliacao: Decimal