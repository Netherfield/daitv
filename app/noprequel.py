
import pymongo


def film_by_year(mydb):
    table = mydb['films']
    print(table)
    result = table.aggregate([
        {"$group" :
            {"_id":"$Year",
             "count":{"$sum":1}}
        },
        {"$sort" : {"_id" : +1}}
    ])
    print(list(result))

def film_by_genre(mydb):
    table = mydb['films']
    result = table.aggregate([
        {
            '$lookup' : {
                'from' : 'moviegenre',
                'localField' : 'MovieID',
                'foreignField' : 'MovieID',
                'as' : 'genrecode'
            }
        },
        {"$unwind" : "$genrecode"},
        {
            '$lookup' : {
                'from' : 'genres',
                'localField' : 'GenreID',
                'foreignField' : 'GenreID',
                'as' : 'genrename'
            }
        },
        {"$unwind" : "$genrename"},
        {"$group" :
            {"_id":"$Name",
             "count":{"$sum":1}}
        },
        {"$sort" : {"_id" : +1}}
    ])
    print(list(result))
    



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
input()
mydb = myclient["daitv"]

# query 1
film_by_genre(mydb)
































