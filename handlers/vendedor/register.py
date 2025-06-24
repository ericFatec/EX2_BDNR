from entities import ( Vendedor, Usuario )
from my_types import ( VendedorCadastroDTO, TipoUsuario )

def register( usuario: Usuario, data: VendedorCadastroDTO ) -> Vendedor:
    vendedor = Vendedor(
        usuario = usuario,
        nome_loja = data.nome_loja.strip() if data.nome_loja and data.nome_loja.strip() else None,
        total_avaliacao = 0.0,
        avaliacoes = [],
        vendas = []
    ).save()

    if TipoUsuario.VENDEDOR.value not in usuario.tipos:
        usuario.tipos.append(TipoUsuario.VENDEDOR.value)
        usuario.save()
    
    return vendedor