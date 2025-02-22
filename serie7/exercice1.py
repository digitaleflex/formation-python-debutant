def creer_personne(nom: str, age: int, ville: str) -> dict:
    """
    Crée un dictionnaire contenant des informations sur une personne.

    Args:
        nom (str): Le nom de la personne.
        age (int): L'âge de la personne.
        ville (str): La ville où réside la personne.

    Returns:
        dict: Un dictionnaire contenant les informations.
    """
    return {"nom": nom, "âge": age, "ville": ville}

# Exemple d'utilisation
if __name__ == "__main__":
    personne = creer_personne("Alice", 30, "Paris")
    print(personne)