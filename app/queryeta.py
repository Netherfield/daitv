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
    query = f"""SELECT u.fasciaeta, r.MovieID, MAX(r.Rating) AS Voto_Massimo, MIN(r.Rating) as Voto_Minimo
    FROM ratings r
    JOIN users u
    ON r.UserID = u.UserID
    WHERE u.fasciaeta = "{e}"
    GROUP BY r.MovieID
    """
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
