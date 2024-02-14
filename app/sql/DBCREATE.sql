drop table moviegenre;
drop table ratings;
drop table films;
drop table genres;
drop table users;

CREATE TABLE genres (
    GenreID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    PRIMARY KEY (GenreID)
);

CREATE TABLE films (
    MovieID INT AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Original VARCHAR(255),
    Year INT NOT NULL,
    PRIMARY KEY (MovieID)
);

CREATE TABLE users (
    UserID INT AUTO_INCREMENT,
    Gender ENUM("M", "F", "X"),
    Age INT CHECK (Age >= 0 AND Age<= 150),
    CAP VARCHAR(10),
    Work VARCHAR(255) NOT NULL,
    PRIMARY KEY (UserID)
);

CREATE TABLE moviegenre (
    MovieGenreID INT AUTO_INCREMENT,
    MovieID INT NOT NULL,
    GenreID INT NOT NULL,
    PRIMARY KEY (MovieGenreID),
    FOREIGN KEY (MovieID) REFERENCES films(MovieID),
    FOREIGN KEY (GenreID) REFERENCES genres(GenreID)
);

CREATE TABLE ratings (
    RatingID INT AUTO_INCREMENT,
    UserID INT NOT NULL,
    MovieID INT NOT NULL,
    Rating INT NOT NULL,
    Timestamp INT,
    PRIMARY KEY (RatingID),
    FOREIGN KEY (MovieID) REFERENCES films(MovieID),
    FOREIGN KEY (UserID) REFERENCES users(UserID)
);