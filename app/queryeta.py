

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

make_list = False
lista_result = list()
unite_query = []
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
    if make_list:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        lista_result.append([e, result])
        conn.close()
    else:
        unite_query.append(query)
if unite_query:
    query = "( " + ") UNION ALL (".join(unite_query) + ")"
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    print(result)
print(lista_result)
