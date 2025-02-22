def compter_caracteres(phrase: str) -> int:
    """
    Compte le nombre de caractères dans une phrase.

    Args:
        phrase (str): La phrase à analyser.

    Returns:
        int: Le nombre de caractères dans la phrase.
    """
    return len(phrase)


def inverser_mot(mot: str) -> str:
    """
    Inverse les lettres d'un mot.

    Args:
        mot (str): Le mot à inverser.

    Returns:
        str: Le mot inversé.
    """
    return mot[::-1]


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


def transformer_phrase(phrase: str) -> tuple:
    """
    Transforme une phrase en majuscules et en minuscules.

    Args:
        phrase (str): La phrase à transformer.

    Returns:
        tuple: Un tuple contenant la phrase en majuscules et en minuscules.
    """
    majuscules = phrase.upper()
    minuscules = phrase.lower()
    return majuscules, minuscules


def remplacer_espaces(phrase: str) -> str:
    """
    Remplace les espaces dans une phrase par des tirets.

    Args:
        phrase (str): La phrase à modifier.

    Returns:
        str: La phrase modifiée avec des tirets à la place des espaces.
    """
    return phrase.replace(" ", "-")


# Tests des fonctions
if __name__ == "__main__":
    # Exercice 1
    phrase = input("Entrez une phrase : ")
    print(f"Nombre de caractères : {compter_caracteres(phrase)}")

    # Exercice 2
    mot = input("Entrez un mot : ")
    print(f"Le mot inversé est : {inverser_mot(mot)}")

    # Exercice 3
    phrase = input("Entrez une phrase : ")
    mot = input("Entrez un mot à rechercher : ")
    if contient_mot(phrase, mot):
        print(f"Le mot '{mot}' est présent dans la phrase.")
    else:
        print(f"Le mot '{mot}' n'est pas présent dans la phrase.")

    # Exercice 4
    phrase = input("Entrez une phrase : ")
    maj, minusc = transformer_phrase(phrase)
    print(f"En majuscules : {maj}")
    print(f"En minuscules : {minusc}")

    # Exercice 5
    phrase = input("Entrez une phrase : ")
    print(f"Phrase modifiée : {remplacer_espaces(phrase)}")