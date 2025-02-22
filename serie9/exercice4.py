class Etudiant:
    def __init__(self, nom, age, moyenne):
        self.nom = nom
        self.age = age
        self.moyenne = moyenne

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Age: {self.age}, Moyenne: {self.moyenne}")

if __name__ == "__main__":
    # Création de plusieurs objets Etudiant
    etudiant1 = Etudiant("Alice", 20, 18.5)
    etudiant2 = Etudiant("Bob", 22, 16.0)

    # Affichage des informations des étudiants
    print("Informations des étudiants :")
    etudiant1.afficher_infos()
    etudiant2.afficher_infos()