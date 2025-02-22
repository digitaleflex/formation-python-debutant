def afficher_elements(dictionnaire: dict) -> None:
    """
    Affiche les clés et les valeurs d'un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire à afficher.
    """
    print("Clés : ", list(dictionnaire.keys()))
    print("Valeurs : ", list(dictionnaire.values()))

# Exemple d'utilisation
if __name__ == "__main__":
    personne = {"nom": "Bob", "âge": 25, "ville": "Lyon"}
    afficher_elements(personne)