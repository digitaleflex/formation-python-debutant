def contient_mot(phrase: str, mot: str) -> bool:
    """
    Vérifie si une chaîne contient un mot donné.

    Args:
        phrase (str): La phrase à analyser.
        mot (str): Le mot à rechercher.

    Returns:
        bool: True si le mot est présent, False sinon.
    """
    return mot in phrase

# Exemple d'utilisation
if __name__ == "__main__":
    phrase = input("Entrez une phrase : ")
    mot = input("Entrez un mot à rechercher : ")
    if contient_mot(phrase, mot):
        print(f"Le mot '{mot}' est présent dans la phrase.")
    else:
        print(f"Le mot '{mot}' n'est pas présent dans la phrase.")