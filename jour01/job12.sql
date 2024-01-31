-- Ajouter Martin Dupuis
INSERT INTO LaPlateforme.etudiant (nom, prenom, age, email) VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

-- Récupérer les membres d'une même famille (Dupuis)
SELECT * FROM LaPlateforme.etudiant WHERE nom = 'Dupuis';