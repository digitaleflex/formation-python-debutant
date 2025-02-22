def saluer(prenom: str) -> None:
    """
    Affiche un message de salutation avec le prénom donné.

    Args:
        prenom (str): Le prénom de la personne à saluer.
    """
    print(f"Bonjour, {prenom} !")

# Exemple d'utilisation
if __name__ == "__main__":
    saluer("Alice")  # Résultat : Bonjour, Alice !