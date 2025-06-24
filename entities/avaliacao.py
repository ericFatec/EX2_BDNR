from mongoengine import Document, StringField, IntField, DateTimeField, ReferenceField

# from .usuario import Usuario
# from .produto import Produto

class Avaliacao(Document):
    usuario = ReferenceField('Usuario', required=False)
    produto = ReferenceField('Produto', required=True)
    nota = IntField(required=True, min_value=0, max_value=5)
    mensagem = StringField(required=True)
    data_avaliacao = DateTimeField(required=True)

    meta = {
        "collection": "avaliacoes"
    }