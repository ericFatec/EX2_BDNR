from pydantic import BaseModel, Field
from datetime import datetime

class AvaliacaoUsuario(BaseModel):
    id: str = Field(alias="_id")
    nome_produto: str
    nota: int
    mensagem: str
    data_avaliacao: datetime