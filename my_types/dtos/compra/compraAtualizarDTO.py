from pydantic import BaseModel
from typing import Dict

class CompraAtualizarDTO(BaseModel):
    itens: Dict[str, int]