from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri="mongodb+srv://admin:admin@cluster0.ufpsji9.mongodb.net/", db_name="mercadolivre"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name):
        return self.db[name]