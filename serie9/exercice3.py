class Personne:
    def __init__(self, nom: str, age: int) -> None:
        self.nom = nom
        self.age = age

    def afficher_infos(self) -> None:
        print(f"Nom : {self.nom}, Age : {self.age}")

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