
CREATE TABLE IF NOT EXISTS films (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Year INT NOT NULL,
    Link TEXT NOT NULL
    );

INSERT INTO films (Title, Year, Link) VALUES
("Bridgerton", 2020, "../static/img/bridgerton.png"),
("Blow", 2001, "../static/img/blow.png"),
("One Piece", 1997, "../static/img/one_piece.png"),
("Mr.Robot", 2015, "../static/img/mrobot.png"),
("C'era una volta in America", 1984, "../static/img/america.png");

