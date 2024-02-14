import mysql.connector

DB_NAME = "daitv"
DB_CONFIG = {"host": "localhost", "user": "root", "password": "", "database": DB_NAME}

def conx():
    return mysql.connector.connect(**DB_CONFIG)

# def range_gender():
def main():
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

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(QUERY_GENDER)
    lista_gender = cursor.fetchall()

    print(lista_eta,lista_gender)

    from itertools import product

    lista_combo = list(product(lista_eta, lista_gender))

    lista_combo = [(a[0], b[0]) for a, b in lista_combo]
    print(lista_combo)
    lista_result = list()
    for f,g in lista_combo:
        print(f,g)
        query = f"""SELECT u.Gender, u.fasciaeta, r.MovieID, AVG(r.Rating) AS avg_rating
        FROM ratings r
        JOIN users u
        ON r.UserID = u.UserID
        WHERE u.Gender = "{g}" AND u.fasciaeta = "{f}"
        GROUP BY r.MovieID
        ORDER BY avg_rating DESC
        LIMIT 10"""
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        lista_result.append([(f,g), result])
        conn.close()
    print(lista_result)

    return lista_result



if __name__ == "__main__":
    main()




