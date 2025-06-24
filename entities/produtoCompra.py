from mongoengine import (
    EmbeddedDocument,
    ObjectIdField,
    StringField,
    DecimalField,
    IntField
)

class ProdutoCompra(EmbeddedDocument):
    id_produto = ObjectIdField(required=True)
    nome_produto = StringField(required=True)
    preco_unitario = DecimalField(required=True, precision=2, min_value=0.01)
    quantidade = IntField(required=True, min_value=1)