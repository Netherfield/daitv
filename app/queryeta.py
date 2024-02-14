

import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "daitv"
    }

QUERY_ETA = "SELECT DISTINCT(fasciaeta) from users"
QUERY_GENDER = "SELECT DISTINCT(Gender) from users"

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
cursor.execute(QUERY_ETA)
lista_eta = cursor.fetchall()

lista_eta = [e[0] for e in lista_eta]

lista_result = list()
for e in lista_eta:
    print(e)
    query = f"""SELECT u.fasciaeta, r.MovieID, AVG(r.Rating) AS avg_rating
    FROM ratings r
    JOIN users u
    ON r.UserID = u.UserID
    WHERE u.fasciaeta = "{e}"
    GROUP BY r.MovieID
    ORDER BY avg_rating DESC
    LIMIT 10"""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    lista_result.append([e, result])
    conn.close()
print(lista_result)
