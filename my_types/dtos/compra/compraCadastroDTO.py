from pydantic import BaseModel
from typing import Dict

class CompraCadastroDTO(BaseModel):
    id_usuario: str
    itens: Dict[str, int]