from entities import ( Compra, Produto, ProdutoCompra, Vendedor )
from typing import Dict, List
from utils import CompraMapper
from copy import deepcopy

def confirm_payment(compra: Compra) -> Compra:
    if compra.pagamento_confirmado:
        return compra
    
    compra.pagamento_confirmado = True
    compra.save()

    produto_ids = [item.id_produto for item in compra.itens]
    produtos = Produto.objects(id__in=produto_ids).only("id", "vendedor")

    produto_para_vendedor: Dict[str, str] = {}
    vendedor_by_id: Dict[str, Vendedor] = {}

    for prod in produtos:
        prod_id = str(prod.id)
        vendedor_id = str(prod.vendedor.id)

        produto_para_vendedor[prod_id] = vendedor_id

        if vendedor_id not in vendedor_by_id:
            vendedor_by_id[vendedor_id] = prod.vendedor

    itens_por_vendedor: Dict[str, List[ProdutoCompra]] = {}

    for item in compra.itens:
        prod_id = str(item.id_produto)
        vendedor_id = produto_para_vendedor.get(prod_id)

        itens_por_vendedor.setdefault(vendedor_id, []).append(item)

    for id_vendedor, vendedor in vendedor_by_id.items():
        itens_do_vendedor = itens_por_vendedor.get(id_vendedor)

        compra_clone = deepcopy(compra)
        compra_clone.itens = itens_do_vendedor

        CompraMapper.toVenda(vendedor, compra_clone)

        vendedor.save()

    return compra