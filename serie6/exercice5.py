def remplacer_espaces(phrase: str) -> str:
    """
    Remplace les espaces dans une phrase par des tirets.

    Args:
        phrase (str): La phrase à modifier.

    Returns:
        str: La phrase modifiée avec des tirets à la place des espaces.
    """
    return phrase.replace(" ", "-")

# Exemple d'utilisation
if __name__ == "__main__":
    phrase = input("Entrez une phrase : ")
    print(f"Phrase modifiée : {remplacer_espaces(phrase)}")