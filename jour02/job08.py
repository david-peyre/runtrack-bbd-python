import mysql.connector

class ZooManager:

    def __init__(self):
        # Établir la connexion à la base de données
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="002003",  
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        # Fermer la connexion à la base de données lorsque l'objet est détruit
        self.cursor.close()
        self.conn.close()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def modifier_animal(self, animal_id, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, animal_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for animal in result:
            print(animal)

    def afficher_animaux_dans_cages(self):
        query = "SELECT a.nom, a.race, c.id AS id_cage FROM animal a LEFT JOIN cage c ON a.id_cage = c.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for animal in result:
            print(animal)

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        superficie_totale = result[0] if result[0] else 0
        print(f"La superficie totale de toutes les cages est de {superficie_totale} m².")

# Exemples d'utilisation
zoo_manager = ZooManager()
zoo_manager.ajouter_animal("Lion", "Africain", 1, "2022-01-01", "Afrique")
zoo_manager.ajouter_animal("Ours", "Grizzly", 2, "2022-02-01", "Amérique du Nord")

zoo_manager.afficher_animaux()

zoo_manager.calculer_superficie_totale()

del zoo_manager  # Ferme la connexion à la base de données
