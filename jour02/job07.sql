-- Création de la base de données
CREATE DATABASE IF NOT EXISTS entreprise;
USE entreprise;

-- Création de la table "employe"
CREATE TABLE IF NOT EXISTS employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id)
);

-- Création de la table "service"
CREATE TABLE IF NOT EXISTS service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);

-- Insertion des employés
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    ('John', 'Doe', 4000, 1),
    ('Jane', 'Doe', 3200, 2),
    ('Bob', 'Smith', 2500, 1);

-- Insertion des services
INSERT INTO service (nom) VALUES
    ('Service A'),
    ('Service B');
