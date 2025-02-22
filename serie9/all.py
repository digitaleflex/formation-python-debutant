class Personne:
    """
    Classe représentant une personne avec un nom et un âge.
    """

    def __init__(self, nom: str, age: int) -> None:
        """
        Initialise une nouvelle instance de la classe Personne.

        Args:
            nom (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.nom = nom
        self.age = age

    def afficher_infos(self) -> None:
        """
        Affiche les informations de la personne.
        """
        print(f"Nom : {self.nom}, Âge : {self.age}")

    @staticmethod
    def comparer_age(personne1: 'Personne', personne2: 'Personne') -> str:
        """
        Compare l'âge de deux objets Personne.

        Args:
            personne1 (Personne): La première personne à comparer.
            personne2 (Personne): La deuxième personne à comparer.

        Returns:
            str: Un message indiquant qui est le plus âgé ou s'ils ont le même âge.
        """
        if personne1.age > personne2.age:
            return f"{personne1.nom} est plus âgé que {personne2.nom}."
        elif personne1.age < personne2.age:
            return f"{personne2.nom} est plus âgé que {personne1.nom}."
        else:
            return f"{personne1.nom} et {personne2.nom} ont le même âge."


class Etudiant(Personne):
    """
    Classe représentant un étudiant, héritant de la classe Personne,
    avec un attribut supplémentaire : note.
    """

    def __init__(self, nom: str, age: int, note: float) -> None:
        """
        Initialise une nouvelle instance de la classe Etudiant.

        Args:
            nom (str): Le nom de l'étudiant.
            age (int): L'âge de l'étudiant.
            note (float): La note de l'étudiant.
        """
        super().__init__(nom, age)
        self.note = note

    def afficher_infos(self) -> None:
        """
        Affiche les informations de l'étudiant, y compris sa note.
        """
        super().afficher_infos()
        print(f"Note : {self.note}")


# Tests des classes et méthodes
if __name__ == "__main__":
    # Exercice 4 : Création et affichage d'étudiants
    etudiant1 = Etudiant("Alice", 20, 18.5)
    etudiant2 = Etudiant("Bob", 22, 16.0)

    print("Informations des étudiants :")
    etudiant1.afficher_infos()
    etudiant2.afficher_infos()

    # Exercice 5 : Comparaison des âges
    personne1 = Personne("Charlie", 30)
    personne2 = Personne("Diana", 25)

    print("\nComparaison des âges :")
    resultat_comparaison = Personne.comparer_age(personne1, personne2)
    print(resultat_comparaison)