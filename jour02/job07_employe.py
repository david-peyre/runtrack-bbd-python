import mysql.connector

class Employe:

    def __enter__(self):
        # Établir la connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="002003",
            database="entreprise"
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Fermer la connexion à la base de données
        self.cursor.close()
        self.conn.close()

    def employe_exists(self, nom, prenom, salaire, id_service):
        # Vérifier si un employé avec les mêmes informations existe déjà
        query = "SELECT id FROM employe WHERE nom = %s AND prenom = %s AND salaire = %s AND id_service = %s"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result is not None

    def create_employe(self, nom, prenom, salaire, id_service):
        # Insérer un nouvel employé dans la base de données
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_employes(self):
        # Récupérer tous les employés de la base de données
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for employe in result:
            print(employe)

    def update_salaire(self, employe_id, new_salaire):
        # Mettre à jour le salaire d'un employé
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_employe(self, employe_id):
        # Supprimer un employé de la base de données
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

# Exemple d'utilisation
with Employe() as employe_manager:
    employe_manager.read_employes()
    employe_manager.create_employe("Bill", "Burr", 3500, 1)
    employe_manager.read_employes()
    employe_manager.update_salaire(3, 4500)
    employe_manager.read_employes()
    employe_manager.delete_employe(1)
    employe_manager.read_employes()
