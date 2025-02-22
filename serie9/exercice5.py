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