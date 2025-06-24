from my_types import ( CompraCadastroDTO )
from entities import ( Compra, Usuario )
from utils import CompraMapper

def register(usuario: Usuario, data: CompraCadastroDTO) -> Compra:
    compra = CompraMapper.toEntity(usuario, data)
    compra.save()

    usuario.compras.append(compra)
    usuario.save()

    return compra