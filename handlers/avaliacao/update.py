from my_types import ( AvaliacaoAtualizarDTO )
from entities import ( Avaliacao )
from utils import AvaliacaoMapper

from .newTotal import nota_editada

def update(avaliacao: Avaliacao, data: AvaliacaoAtualizarDTO) -> Avaliacao:
    nota_anterior = avaliacao.nota

    AvaliacaoMapper.updateAvaliacao(avaliacao, data)

    produto = avaliacao.produto
    produto.total_avaliacao = nota_editada(
        len(produto.avaliacoes), produto.total_avaliacao, avaliacao.nota, nota_anterior
    )
    produto.save()

    vendedor = produto.vendedor
    vendedor.total_avaliacao = nota_editada(
        len(vendedor.avaliacoes), vendedor.total_avaliacao, avaliacao.nota, nota_anterior
    )
    vendedor.save()

    return avaliacao.save()