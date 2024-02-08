import mysql.connector

class Service:

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

    def create_service(self, nom):
        # Insérer un nouveau service dans la base de données
        query = "INSERT INTO service (nom) VALUES (%s)"
        values = (nom,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_services(self):
        # Récupérer tous les services de la base de données
        query = "SELECT * FROM service"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for service in result:
            print(service)

# Exemple d'utilisation
with Service() as service_manager:
    service_manager.create_service("Service C")
    service_manager.read_services()
