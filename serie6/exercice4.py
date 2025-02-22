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

# Exemple d'utilisation
if __name__ == "__main__":
    phrase = input("Entrez une phrase : ")
    maj, minusc = transformer_phrase(phrase)
    print(f"En majuscules : {maj}")
    print(f"En minuscules : {minusc}")