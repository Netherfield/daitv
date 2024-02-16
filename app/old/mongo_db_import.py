import time
import pandas as pd
from pymongo import MongoClient


from secret import uri_mongodb

def load_data(uri_mongodb, nome_db, nome_collezione, path_csv=None): # -> path_csv = str (csv path) or dict (documents)
    try:
        client = MongoClient(uri_mongodb)
        db = client[nome_db]
        collection = db[nome_collezione]
        if isinstance(path_csv, str): # path csv
            dati = pd.read_csv(path_csv)
            collection.insert_many(dati.to_dict('records'))
        elif isinstance(path_csv, dict): # dizionario
            dati = path_csv
            collection.insert_one(dati)
        else:
            print("Formato dati input non valido")
            return None
    except Exception as e:
        print(f"Errore: {e}")

def create(uri_mongodb):
    try:
        client = MongoClient(uri_mongodb)
        db_list = client.list_database_names()
        db_name = input("inserisci nome DB: ")
        db = client[db_name]
        if db_name in db_list:
            print("Connesso al DB")
        else:
            print("DB creato")
        collec = input("Inserisci nome collezione: ")
        collec_list = db.list_collection_names()
        collection = db[collec]
        if collec in collec_list:
            print("Connesso alla collezione")
        else:
            collection.insert_one({"data_creazione": time.time(), "nome_db": db_name, "collection": collec })
            print("Collezione creata")
    except Exception as e:
        print(f"Errore: {e}")


