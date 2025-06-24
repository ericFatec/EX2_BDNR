from mongoengine import (
    EmbeddedDocument,
    ObjectIdField,
    StringField,
    DateTimeField,
    EmbeddedDocumentListField,
)

from .produtoCompra import ProdutoCompra

class Venda(EmbeddedDocument):
    id = ObjectIdField(required=True)
    id_usuario = ObjectIdField(required=True)
    nome_usuario = StringField(required=True)
    data_compra = DateTimeField(required=True)
    itens = EmbeddedDocumentListField(ProdutoCompra, required=True)