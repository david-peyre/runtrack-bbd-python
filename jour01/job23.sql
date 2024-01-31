SELECT *
FROM LaPlateforme.etudiant
WHERE age = (SELECT MAX(age) FROM LaPlateforme.etudiant);
