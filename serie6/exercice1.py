def compter_caracteres(phrase: str) -> int:
    """
    Compte le nombre de caractères dans une phrase.

    Args:
        phrase (str): La phrase à analyser.

    Returns:
        int: Le nombre de caractères dans la phrase.
    """
    return len(phrase)

# Exemple d'utilisation
if __name__ == "__main__":
    phrase = input("Entrez une phrase : ")
    print(f"Nombre de caractères : {compter_caracteres(phrase)}")