from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List

from .produtoCompraDTO import ProdutoCompraDTO

class CompraDTO(BaseModel):
    id: str = Field(alias="_id")
    id_usuario: str
    nome_usuario: str
    data_compra: datetime
    total: Decimal
    itens: List[ProdutoCompraDTO]
    pagamento_confirmado: bool