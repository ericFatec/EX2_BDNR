from my_types import ( ProdutoDTO, Favorito, ProdutoVendedor, ProdutoLoadedDTO, ProdutoCadastroDTO, ProdutoAtualizarDTO )
from entities import ( Produto, ProdutoCompra )

from .avaliacaoMapper import AvaliacaoMapper

class ProdutoMapper:
    @staticmethod
    def toEntity(novo_produto: ProdutoCadastroDTO) -> Produto:
        produto = Produto(
            nome = novo_produto.nome.strip() if novo_produto.nome and novo_produto.nome.strip() else None,
            descricao = novo_produto.descricao.strip() if novo_produto.descricao and novo_produto.descricao.strip() else None,
            preco = novo_produto.preco,
            estoque = novo_produto.estoque if novo_produto.estoque else 0,
            total_avaliacao = 0.0,
            avaliacoes = []
        )

        return produto

    @staticmethod
    def toDTO(produto: Produto) -> ProdutoDTO:
        vendedor = produto.vendedor

        produtoDTO = ProdutoDTO(
            _id = str(produto.pk),
            id_vendedor = str(vendedor.pk),
            nome_loja = vendedor.nome_loja,
            nome = produto.nome,
            descricao = produto.descricao,
            preco = produto.preco,
            estoque = produto.estoque,
            total_avaliacao = produto.total_avaliacao,
            avaliacoes = len(produto.avaliacoes)
        )

        return produtoDTO
    
    @staticmethod
    def toLoadedDTO(produto: Produto) -> ProdutoLoadedDTO:
        vendedor = produto.vendedor

        produtoDTO = ProdutoDTO(
            _id = str(produto.pk),
            id_vendedor = str(vendedor.pk),
            nome_loja = vendedor.nome_loja,
            nome = produto.nome,
            descricao = produto.descricao,
            preco = produto.preco,
            estoque = produto.estoque,
            total_avaliacao = produto.total_avaliacao,
            avaliacoes = [AvaliacaoMapper.toDTO(a) for a in produto.avaliacoes]
        )

        return produtoDTO
    
    @staticmethod
    def updateProduto(produto: Produto, data: ProdutoAtualizarDTO) -> Produto:
        if data.nome and data.nome.strip():
            produto.nome = data.nome.strip()
        if data.descricao and data.descricao.strip():
            produto.descricao = data.descricao.strip()
        if data.preco is not None:
            produto.preco = data.preco
        if data.estoque is not None:
            produto.estoque = data.estoque

        return produto
    
    @staticmethod
    def toProdCompra(produto: Produto, quantidade: int) -> ProdutoCompra:
        produtoCompra = ProdutoCompra(
            id_produto = str(produto.pk),
            nome_produto = produto.nome,
            preco_unitario = produto.preco,
            quantidade = quantidade
        )

        return produtoCompra
    
    @staticmethod
    def toFavorite(produto: Produto) -> Favorito:
        favorito = Favorito(
            _id = str(produto.pk),
            nome = produto.nome,
            preco = produto.preco,
            estoque = produto.estoque,
            total_avaliacao = produto.total_avaliacao
        )

        return favorito
    
    @staticmethod
    def toProdVendedor(produto: Produto) -> ProdutoVendedor:
        prodVendedor = ProdutoVendedor(
            _id = str(produto.pk),
            nome = produto.nome,
            descricao = produto.descricao,
            preco = produto.preco,
            estoque = produto.estoque,
            total_avaliacao = produto.total_avaliacao
        )

        return prodVendedor