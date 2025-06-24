from my_types import ( PerfilVendedor, VendedorDTO, VendedorLoadedDTO )
from entities import ( Vendedor, Produto )
from typing import Optional

from .produtoMapper import ProdutoMapper
from .compraMapper import CompraMapper
from .avaliacaoMapper import AvaliacaoMapper

class VendedorMapper:
    @staticmethod
    def toDTO(vendedor: Vendedor) -> VendedorDTO:
        vendedorDTO = VendedorDTO(
            _id = str(vendedor.pk),
            id_usuario = str(vendedor.usuario.id),
            nome_usuario = vendedor.usuario.nome,
            nome_loja = vendedor.nome_loja,
            total_avaliacao = vendedor.total_avaliacao,
            avaliacoes = len(vendedor.avaliacoes),
            vendas = len(vendedor.vendas)
        )

        return vendedorDTO
    
    @staticmethod
    def toLoadedDTO(vendedor: Vendedor) -> VendedorLoadedDTO:

        vendedorDTO = VendedorLoadedDTO(
            _id = str(vendedor.pk),
            id_usuario = str(vendedor.usuario.id),
            nome_usuario = vendedor.usuario.nome,
            nome_loja = vendedor.nome_loja,
            total_avaliacao = vendedor.total_avaliacao,
            avaliacoes = [AvaliacaoMapper.toDTO(a) for a in vendedor.avaliacoes],
            vendas = [CompraMapper.toVendaDTO(v) for v in vendedor.vendas],
            produtos = [ProdutoMapper.toProdVendedor(p) for p in vendedor.produtos]
        )

        return vendedorDTO

    @staticmethod
    def toPerfil(vendedor: Vendedor) -> Optional[PerfilVendedor]:
        if not vendedor:
            return None

        perfil = PerfilVendedor(
            _id = str(vendedor.pk),
            nome_loja = vendedor.nome_loja,
            total_avaliacao = vendedor.total_avaliacao,
            avaliacoes = len(vendedor.avaliacoes),
            vendas = len(vendedor.vendas)
        )

        return perfil