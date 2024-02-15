import pandas as pd
from pymongo import MongoClient

def load_data(uri_mongodb, nome_db, nome_collezione, path_csv):
    client = MongoClient(uri_mongodb)
    db = client[nome_db]
    collection = db[nome_collezione]
    dati = pd.read_csv(path_csv)
    collection.insert_many(dati.to_dict('records'))


nome_db = "DAITV2"
nome_collezione = "films"
path = "films.csv"

load_data(uri_mongodb, nome_db, nome_collezione, path)