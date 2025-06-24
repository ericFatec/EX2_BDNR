from pydantic import BaseModel

class VendedorCadastroDTO(BaseModel):
    id_usuario: str
    nome_loja: str