from my_types import ( CompraDTO, ProdutoCompraDTO, CompraCadastroDTO, CompraAtualizarDTO, VendaDTO )
from entities import ( Compra, ProdutoCompra, Venda, Vendedor, Usuario, Produto )
from datetime import datetime
from typing import Dict, List
from decimal import Decimal

from .produtoMapper import ProdutoMapper

class CompraMapper:
    @staticmethod
    def toEntity(usuario: Usuario, data: CompraCadastroDTO) -> Compra:
        produtos_by_id = CompraMapper._pullProdutos([pid for pid in data.itens.keys()])

        itens_compra = []
        total = Decimal("0")
        for prod_id, quantidade in data.itens.items():
            produto = produtos_by_id.get(prod_id)

            item = ProdutoMapper.toProdCompra(produto, quantidade)
            total += Decimal(item.quantidade) * item.preco_unitario
            
            itens_compra.append(item)

        compra = Compra(
            usuario = usuario,
            data_compra = datetime.now(),
            total = total,
            itens = itens_compra,
            pagamento_confirmado = False
        )

        return compra

    @staticmethod
    def toDTO(compra: Compra) -> CompraDTO:
        compraDTO = CompraDTO(
            _id = str(compra.pk),
            id_usuario = str(compra.usuario.id),
            nome_usuario = compra.usuario.nome,
            data_compra = compra.data_compra,
            total = compra.total,
            itens = [CompraMapper._toProdCompra(p) for p in compra.itens],
            pagamento_confirmado = compra.pagamento_confirmado
        )

        return compraDTO
    
    @staticmethod
    def updateCompra(compra: Compra, data: CompraAtualizarDTO) -> Compra:
        itens_existentes_by_id = {str(item.id_produto): item for item in compra.itens}

        novos_ids = [pid for pid in data.itens.keys() if pid not in itens_existentes_by_id]

        if novos_ids:
            produtos_by_id = CompraMapper._pullProdutos([pid for pid in novos_ids])
        else:
            produtos_by_id = {}

        total = Decimal("0")
        for prod_id, quantidade in data.itens.items():
            if prod_id in itens_existentes_by_id:
                item = itens_existentes_by_id[prod_id]

                if quantidade <= 0:
                    compra.itens.remove(item)
                else:
                    item.quantidade = quantidade
            elif quantidade > 0:
                produto = produtos_by_id.get(prod_id)
                if produto is None:
                    raise ValueError(f"Produto {prod_id} não encontrado para adicionar.")
                novo_item = ProdutoMapper.toProdCompra(produto, quantidade)
                compra.itens.append(novo_item)

        for item in compra.itens:
            total += Decimal(item.quantidade) * item.preco_unitario

        compra.total = total

        return compra
    
    @staticmethod
    def toVenda(vendedor: Vendedor, compra: Compra) -> Vendedor:
        venda = Venda(
            id = str(compra.pk),
            id_usuario = str(compra.usuario.id),
            nome_usuario = compra.usuario.nome,
            data_compra = compra.data_compra,
            itens = compra.itens
        )

        vendedor.vendas.append(venda)
        return vendedor
    
    def toVendaDTO(venda: Venda) -> VendaDTO:
        vendaDTO = VendaDTO(
            _id = str(venda.id),
            id_usuario = str(venda.id_usuario),
            nome_usuario = venda.nome_usuario,
            data_compra = venda.data_compra,
            itens = [CompraMapper._toProdCompra(p) for p in venda.itens]
        )

        return vendaDTO
    
    @staticmethod
    def _toProdCompra(produto: ProdutoCompra) -> ProdutoCompraDTO:
        produtoDTO = ProdutoCompraDTO(
            id_produto = str(produto.id_produto),
            nome_produto = produto.nome_produto,
            preco_unitario = produto.preco_unitario,
            quantidade = produto.quantidade
        )

        return produtoDTO
    
    @staticmethod
    def _pullProdutos(ids: List[str]) -> Dict[str, Produto]:
        produtos = Produto.objects(id__in=ids)
        produtos_by_id: Dict[str, Produto] = {
            str(prod.id): prod for prod in produtos
        }

        return produtos_by_id