from pymongo import MongoClient

# Connessione al server MongoDB
client = MongoClient("mongodb://localhost:27017/")
input()
db = client['daitv']
films_collection = db['films']
films = db['films']

# Esecuzione della query di aggregazione
"""
id:0 = non visualizzare
numero_films:1 = includi nel risultato
year:_id = rinomina id come year (id era il nostro year poiche _id : year)
quindi project dice, non visualizzare _id e quello che prima era _id chiamalo year
"""
if False:
    result = films.aggregate([
        {"$group": {"_id": "$Year", "numero_films": {"$sum": 1}}},
        {"$sort" : {"_id" : +1}},
        {"$project": {"_id": 0, "Year": "$_id", "numero_films": 1}}
        ])
    # Stampa dei risultati
    for item in result:
        print(item)

if False:
    result = db['ratings'].aggregate([
        {
            "$match":{"Rating":{"$lte":3}
    }
    },

    {
            "$group": {"_id":"$MovieID", "low_scoring": {"$sum":1}
        }
    },
        {
            "$match":{"low_scoring":{"$gte": 250}
        }
    },
            {"$lookup": { "from": "films", 
                        "localField": "_id", 
                        "foreignField": "MovieID",
                        "as": "dati_film"
        }
    },
            {"$unwind": "$dati_film"},
        {
            "$project":
                {
                    "_id" : 0,
                    "MovieID" : "$_id",
                    "Title":"$dati_film.Title",
                    "low_scoring":1
                }
        }
    ])
    for item in result:
        print(item)

if False:
    "b)il numero di film per ogni genere"
    """
    filter : moviegenres
    """
    result = films.aggregate([
        {
            "$lookup": {
                "from": "moviegenre",
                "localField": "MovieID",
                "foreignField": "MovieID",
                "as": "moviegenres"
            }
        },
        {
            "$group": {
                "_id": "$GenreID",
                "numero_films": { "$sum": 1 }
            }
        },
        {
            "$lookup" : {
                "from": "genres",
                "localField": "GenreID",
                "foreignField": "GenreID",
                "as": "movies"
            }
        },
        {
            "$project": {
                "_id": 0,
                "Genre": "$_id",
                "numero_films": 1
            }
        }
    ])

    for item in result:
        print(item)


if False:
    "c)il numero degli abbonati in base al lavoro"

    result2 = [
        {
            "$group": {
                "_id": "$work",
                "numero_abbonati": {"$sum": 1}
            }
        }
    ]

    result = list(db['users'].aggregate(result2))
    for item in result:
        print(item)



