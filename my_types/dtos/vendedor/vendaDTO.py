from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List

from ..compra.produtoCompraDTO import ProdutoCompraDTO

class VendaDTO(BaseModel):
    id: str = Field(alias="_id")
    id_usuario: str
    nome_usuario: str
    data_compra: datetime
    itens: List[ProdutoCompraDTO]