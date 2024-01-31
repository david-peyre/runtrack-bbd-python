import mysql.connector

# Paramètres de connexion à la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '002003',
    'database': 'LaPlateforme'
}

# Connexion à la base de données
connection = mysql.connector.connect(**db_config)

try:
    # Création d'un objet curseur pour exécuter des requêtes SQL
    cursor = connection.cursor()

    # Exécution de la requête SQL pour récupérer tous les étudiants
    query = "SELECT * FROM etudiant;"
    cursor.execute(query)

    # Récupération de tous les résultats
    students = cursor.fetchall()

    # Affichage des résultats
    for student in students:
        print(student)

finally:
    # Fermeture du curseur et de la connexion
    cursor.close()
    connection.close()
