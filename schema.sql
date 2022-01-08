DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
);

INSERT INTO user (username) VALUES ("djs"), ("django"), ("steve"), ("lily");