import mongoengine

class MongoConnection:
    MONGODB_URI = "mongodb://localhost:27017/"
    MONGODB_DB  = "mercadolivre"

    def __init__(self, uri=MONGODB_URI, db_name=MONGODB_DB, alias="default"):
        self.uri = uri
        self.db_name = db_name
        self.alias = alias
        self.connect()

    def connect(self):
        mongoengine.connect(
            db=self.db_name,
            host=self.uri,
            alias=self.alias
        )

    def disconnect(self):
        mongoengine.disconnect(alias=self.alias)