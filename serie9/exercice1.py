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