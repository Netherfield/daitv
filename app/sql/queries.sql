
-- ratings x voto
CREATE VIEW fascia_and_movieid_avg AS
SELECT u.fasciaeta, AVG(r.Rating) AS avg_rating, r.MovieID
	FROM users u
	JOIN ratings r
 		ON r.UserID = u.UserID
	GROUP BY u.fasciaeta, r.MovieID;

-- poi per visualizzare la categoria
-- per vederle tutte usare queryeta.py
SELECT a.fasciaeta, f.MovieID, a.avg_rating
FROM fascia_and_movieid_avg a
JOIN films f
	ON a.MovieID = f.MovieID
WHERE a.fasciaeta = '18-24'
ORDER BY a.avg_rating DESC
LIMIT 10;



SELECT f.Title as Titolo, e.best AS Migliore, e.worst AS Peggiore, e.fasciaeta AS Fascia_Eta
FROM films f
    JOIN (
            SELECT MAX(a.Voto_Medio) as best, MIN(a.Voto_Medio) as worst, a.fasciaeta, a.MovieID
            FROM avg_rating_by_agerange_and_movieid a
        	GROUP BY a.fasciaeta
        ) AS e
        ON e.MovieID = f.MovieID;

-- movies by year
SELECT Year, COUNT(*) AS numero_films
FROM films
GROUP BY Year

-- movies by genre
SELECT genres.Name, COUNT(moviegenre.MovieID) AS numero_films
FROM genres
JOIN moviegenre ON genres.GenreID = moviegenre.GenreID
GROUP BY genres.GenreID;

-- movies by work
SELECT work, COUNT(*) AS numero_abbonati
FROM users
GROUP BY work

-- top 10 by agerange and gender
-- vedi queries.py


-- movies with more than 250 ratings under 3
SELECT f.Title, b.bad_scores
FROM (SELECT ratings.MovieID, COUNT(MovieID) as bad_scores
from ratings
WHERE ratings.Rating <= 3
GROUP BY ratings.MovieID) AS b
JOIN films f
	ON b.MovieID = f.MovieID
WHERE bad_scores >= 250;


-- by province
SELECT province.Provincia , users.CAP AS CAP, COUNT(users.UserID) as Numero_Iscritti
FROM users
JOIN province ON users.CAP = province.CAP
GROUP BY province.Provincia
ORDER BY Numero_Iscritti DESC
LIMIT 20;

