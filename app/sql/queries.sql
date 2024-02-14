
-- ratings x voto
SELECT COUNT(r.Rating)
FROM ratings r
    JOIN users u
        ON r.UserID = u.UserID
    GROUP BY u.fasciaeta


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


-- movies with more than 250 ratings under 3

-- by province

SELECT province.Provincia , users.CAP AS CAP, COUNT(users.UserID) as Numero_Iscritti
FROM users
JOIN province ON users.CAP = province.CAP
GROUP BY province.Provincia
ORDER BY Numero_Iscritti DESC
LIMIT 20;

