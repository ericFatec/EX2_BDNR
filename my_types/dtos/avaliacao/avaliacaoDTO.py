from pydantic import BaseModel, Field
from datetime import datetime

class AvaliacaoDTO(BaseModel):
    id: str = Field(alias="_id")
    nome_usuario: str
    nome_produto: str
    nota: int
    mensagem: str
    data_avaliacao: datetime