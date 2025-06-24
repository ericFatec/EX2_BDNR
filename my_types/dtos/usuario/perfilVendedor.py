from pydantic import BaseModel, Field
from decimal import Decimal

class PerfilVendedor(BaseModel):
    id: str = Field(alias="_id")
    nome_loja: str
    total_avaliacao: Decimal
    avaliacoes: int
    vendas: int