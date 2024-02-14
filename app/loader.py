import mysql.connector
import csv

DB_NAME = "daitv"
DB_CONFIG = {"host": "localhost", "user": "root", "password": "", "database": DB_NAME}
def conx():
    return mysql.connector.connect(**DB_CONFIG)

def users():
    QUERY = "INSERT INTO users (UserID, Gender, Age, CAP, Work) VALUES (%s, %s, %s, %s, %s)"

    with open("drop/users_edit.csv") as file:
        reader = csv.reader(file)
        next(reader)
        # print(list(reader))
        connection = conx()
        cursor = connection.cursor()
        cursor.executemany(QUERY, list(reader))
        connection.commit()

def ratings():
    QUERY = "INSERT INTO Ratings (UserID, MovieID, Rating, Timestamp) VALUES (%s, %s, %s, %s)"
    with open("drop/ratings_edit.csv") as file:
        reader = csv.reader(file)
        next(reader)
        # print(list(reader))
        connection = conx()
        cursor = connection.cursor()
        import app.core.compiler as t
        all = list(reader)
        for chunk in t.batch(all, 5000):
            cursor.executemany(QUERY, chunk)
            connection.commit()
            print("done 5000")
