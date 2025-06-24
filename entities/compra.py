from mongoengine import (
    Document,
    DateTimeField,
    DecimalField,
    EmbeddedDocumentListField,
    ReferenceField,
    BooleanField
)

from .produtoCompra import ProdutoCompra
# from .usuario import Usuario

class Compra(Document):
    usuario = ReferenceField('Usuario', required=True)
    data_compra = DateTimeField(required=True)
    total = DecimalField(required=True, precision=2, min_value=0.01)
    itens = EmbeddedDocumentListField(ProdutoCompra, required=True)
    pagamento_confirmado = BooleanField(required=True)

    meta = {
        "collection": "compras"
    }