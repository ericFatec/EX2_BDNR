from pydantic import BaseModel, Field
from decimal import Decimal

class VendedorDTO(BaseModel):
    id: str = Field(alias="_id")
    id_usuario: str
    nome_usuario: str
    nome_loja: str
    total_avaliacao: Decimal
    avaliacoes: int
    vendas: int