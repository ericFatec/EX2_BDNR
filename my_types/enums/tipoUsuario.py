from enum import Enum


class TipoUsuario(str, Enum):
    CLIENTE = "cliente"
    VENDEDOR = "vendedor"