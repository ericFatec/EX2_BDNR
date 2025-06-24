from pydantic import BaseModel

class AvaliacaoCadastroDTO(BaseModel):
    id_usuario: str
    id_produto: str
    nota: int
    mensagem: str