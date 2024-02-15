# Copyright (c) 2023 Jules aka Netherfield
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
    make_list = False
    lista_result = list()
    unite_query = []
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
        if make_list:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            lista_result.append([(f,g), result])
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
    for elem in lista_result:
        print(elem[0])
        for e in elem[1]:
            print(e)
    print(result)
    return lista_result



if __name__ == "__main__":
    main()




