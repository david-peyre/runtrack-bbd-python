import mysql.connector

# Configuration de la connexion à la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '002003',  # Remplacez par votre mot de passe
    'database': 'LaPlateforme'
}

# Établir la connexion
connection = mysql.connector.connect(**db_config)

# Créer un curseur
cursor = connection.cursor()

try:
    # Sélectionner les noms et les capacités de la table "salle"
    query = "SELECT nom, capacite FROM salle"
    cursor.execute(query)

    # Récupérer les résultats
    result = cursor.fetchall()

    # Afficher les résultats
    for row in result:
        print(f"Nom: {row[0]}, Capacité: {row[1]}")

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    # Fermer le curseur et la connexion
    cursor.close()
    connection.close()
