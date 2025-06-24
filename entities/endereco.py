from mongoengine import EmbeddedDocument, StringField

class Endereco(EmbeddedDocument):
    cep = StringField(required=True)
    numero = StringField(required=True)