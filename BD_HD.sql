CREATE DATABASE cesar_db;

USE cesar_db;

CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original TEXT NOT NULL,
    cifrado TEXT NOT NULL
);

SELECT * FROM mensajes;
