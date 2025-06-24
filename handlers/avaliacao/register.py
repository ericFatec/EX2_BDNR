from entities import ( Avaliacao, Usuario, Produto, Compra )
from my_types import ( AvaliacaoCadastroDTO )

from utils import AvaliacaoMapper
from .newTotal import nova_nota

def register(data: AvaliacaoCadastroDTO) -> Avaliacao:
    usuario = Usuario.objects(pk=data.id_usuario).first()
    produto = Produto.objects(pk=data.id_produto).first()

    produto_comprado = Compra.objects(
        usuario=usuario,
        itens__match={"id_produto": produto.id}
    ).first()

    if not produto_comprado:
        raise ValueError("Usuário só pode avaliar produtos comprados")

    avaliacao = AvaliacaoMapper.toEntity(usuario, produto, data)
    avaliacao.save()

    vendedor = produto.vendedor

    usuario.avaliacoes.append(avaliacao)
    usuario.save()

    produto.avaliacoes.append(avaliacao)
    produto.total_avaliacao = nova_nota(
        len(produto.avaliacoes), produto.total_avaliacao, avaliacao.nota
    )
    produto.save()

    vendedor.avaliacoes.append(avaliacao)
    vendedor.total_avaliacao = nova_nota(
        len(vendedor.avaliacoes), vendedor.total_avaliacao, avaliacao.nota
    )
    vendedor.save()

    return avaliacao