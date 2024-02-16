
import csv

from web.connection import read_query, create_db_connection

def write_to_csv(path, query, titles):
    try:
        fp = open(path, "x", encoding="utf-8", newline="")
    except:
        fp = open(path, "w", encoding="utf-8", newline="")
    writer = csv.writer(fp)
    writer.writerow(titles)

    conn = create_db_connection("localhost", "root", "", "daitv")
    result = read_query(conn, query)
    for elem in result:
        print(elem)
        writer.writerow(elem)
    fp.close()

def gen_to_csv(path, gen, titles):
    try:
        fp = open(path, "x", encoding="utf-8", newline="")
    except:
        fp = open(path, "w", encoding="utf-8", newline="")
    writer = csv.writer(fp)
    writer.writerow(titles)
    for chunk in gen:
        writer.writerows(chunk)
    fp.close()


BY_YEAR = """SELECT Year, COUNT(*) AS numero_films
FROM films
GROUP BY Year"""
BY_GENRE = """SELECT genres.Name, COUNT(moviegenre.MovieID) AS numero_films
FROM genres
JOIN moviegenre ON genres.GenreID = moviegenre.GenreID
GROUP BY genres.GenreID;"""
TO_DELETE = """SELECT f.Title, b.Voti, b.avg_rating
FROM (SELECT ratings.MovieID, AVG(Rating) as avg_rating, COUNT(ratings.MovieID) as Voti
from ratings
GROUP BY ratings.MovieID
HAVING COUNT(ratings.MovieID) > 250) AS b
JOIN films f
	ON b.MovieID = f.MovieID
WHERE b.avg_rating < 3;"""
BY_PROVINCE = """SELECT province.Provincia , users.CAP AS CAP, COUNT(users.UserID) as Numero_Iscritti
FROM users
JOIN province ON users.CAP = province.CAP
GROUP BY province.Provincia
ORDER BY Numero_Iscritti DESC
LIMIT 20;"""
BY_WORK = """SELECT work, COUNT(*) AS numero_abbonati
FROM users
GROUP BY work
"""

# write_to_csv("./per_anno.csv", BY_YEAR, ["Year", "Numero Films"])
# write_to_csv("per_genere.csv", BY_GENRE, ["Genere", "Numero Films"])
# write_to_csv("da_eliminare.csv", TO_DELETE, ["Titolo", "Numero Voti", "Voto Medio"])
# write_to_csv("per_provincia.csv", BY_PROVINCE, ["Provincia", "CAP", "Numero Iscritti"])
# write_to_csv("per_lavoro.csv", BY_WORK, ["Lavoro", "Numero Iscritti"])


import queries, queryeta
aglist = queries.age_gender()
gen_to_csv("agerange_gender_morethan.csv", aglist, ["Gender", "Fasciaeta", "ID Film", "Voti", "Voto Medio"])
# alist = queryeta.by_age()
# gen_to_csv("age_gender.csv", alist, ["Fasciaeta", "ID Film", "Voto Massimo", "Voto Minimo"])




















