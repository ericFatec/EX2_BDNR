from pydantic import BaseModel
from typing import Optional

class AvaliacaoAtualizarDTO(BaseModel):
    nota: Optional[int]
    mensagem: Optional[str]