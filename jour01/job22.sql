SELECT *
FROM LaPlateforme.etudiant
WHERE age = (SELECT MIN(age) FROM LaPlateforme.etudiant);
