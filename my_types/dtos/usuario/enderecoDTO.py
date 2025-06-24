from pydantic import BaseModel

class EnderecoDTO(BaseModel):
    cep: str
    numero: str