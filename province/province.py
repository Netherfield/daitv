import mysql.connector
import csv

DB_NAME = "DAITV"
DB_CONFIG = {"host": "localhost", "user": "root", "password": "", "database": DB_NAME}
QUERY = "INSERT INTO province (Comune, Provincia, CAP) VALUES (%s, %s, %s)"

def conx():
    return mysql.connector.connect(**DB_CONFIG)

conn = conx()
cursor = conn.cursor()
cursor.execute("""CREATE TABLE province (
Comune VARCHAR(255) NOT NULL,
Provincia VARCHAR(10) NOT NULL,
CAP VARCHAR(10) NOT NULL
);""")

with open("province/province.csv") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    connection = conx()
    cursor = connection.cursor()
    cursor.executemany(QUERY, list(reader))
    connection.commit()
