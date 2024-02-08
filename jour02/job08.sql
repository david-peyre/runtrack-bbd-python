-- Création de la base de données
CREATE DATABASE IF NOT EXISTS zoo;

-- Utilisation de la base de données
USE zoo;

-- Création de la table "animal"
CREATE TABLE IF NOT EXISTS animal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    race VARCHAR(255),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255),
    FOREIGN KEY (id_cage) REFERENCES cage(id)
);

-- Création de la table "cage"
CREATE TABLE IF NOT EXISTS cage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    superficie DECIMAL(10, 2) NOT NULL,
    capacite_max INT NOT NULL
);
