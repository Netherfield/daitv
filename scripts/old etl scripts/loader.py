# Copyright (c) 2023 Pavlo
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
