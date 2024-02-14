import mysql.connector


"""
E ○    il numero di film per ogni anno 
E ○   il numero di film per ogni genere

D ○    i film che hanno recensioni al di sotto di 3 per un numero 250 di persone in modo da eliminarli

F ○    la top 10 per ogni intervallo di età e sesso

J ○    rating film - i voti dal meno preferito al più preferito per fasce di età

P ○    il numero degli iscritti alla piattaforma nelle varie province, voglio vedere le prime 20

E ○    il numero degli abbonati in base al lavoro
"""
RATING = """


"""

PROVINCE = """SELECT CAP, COUNT(UserID) as Numero_Iscritti
FROM users
GROUP BY CAP
ORDER BY Numero_Iscritti DESC
LIMIT 20;"""

DB_NAME = "daitv"
DB_CONFIG = {"host": "localhost", "user": "root", "password": "", "database": DB_NAME}

def conx():
    return mysql.connector.connect(**DB_CONFIG)


def run():
    connection = conx()
    cursor = connection.cursor()
    cursor.execute(RATING)






