def inverser_mot(mot: str) -> str:
    """
    Inverse les lettres d'un mot.

    Args:
        mot (str): Le mot à inverser.

    Returns:
        str: Le mot inversé.
    """
    return mot[::-1]

# Exemple d'utilisation
if __name__ == "__main__":
    mot = input("Entrez un mot : ")
    print(f"Le mot inversé est : {inverser_mot(mot)}")