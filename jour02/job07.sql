-- Création de la base de données
CREATE DATABASE IF NOT EXISTS entreprise;

-- Utilisation de la base de données
USE entreprise;

-- Création de la table "employe"
CREATE TABLE IF NOT EXISTS employe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

-- Insertion d'employés dans la table "employe"
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
    ('Spinoza', 'Baruch', 2500.00, 1),
    ('Weil', 'Simone', 5800.50, 2),
    ('Nietzsche', 'Fredrich', 4000.75, 1);

-- Création de la table "service"
CREATE TABLE IF NOT EXISTS service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

-- Insertion de services dans la table "service"
INSERT INTO service (nom) VALUES
    ('Ressources humaines'),
    ('Service Informatique');

-- Récupérer tous les employés dont le salaire est supérieur à 3 000 € :
SELECT * FROM employe WHERE salaire > 3000.00;

-- Récupérer tous les employés et leur service respectif :
SELECT employe.*, service.nom AS service_nom
FROM employe
JOIN service ON employe.id_service = service.id;
