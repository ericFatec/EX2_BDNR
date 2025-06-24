from bson import ObjectId
from entities import (
    Vendedor,
    Compra
)

def sync_name(id: str, new_name: str) -> None:

    compra_ids = list(
        Compra.objects(usuario=id).scalar("id")
    )

    affected_vendedores = Vendedor.objects(vendas__id__in=compra_ids)
    for vendedor in affected_vendedores:
        changed = False
        for venda in vendedor.vendas:
            if venda.id in compra_ids:
                venda.nome_usuario = new_name
                changed = True
        if changed:
            vendedor.save()