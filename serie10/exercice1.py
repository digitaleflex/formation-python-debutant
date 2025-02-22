import random
import string

def generer_mot_de_passe(longueur: int) -> str:
    """
    Génère un mot de passe aléatoire.

    Args:
        longueur (int): La longueur du mot de passe.

    Returns:
        str: Un mot de passe aléatoire.
    """
    if longueur < 4:
        raise ValueError("La longueur du mot de passe doit être au moins de 4 caractères.")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        longueur = int(input("Entrez la longueur du mot de passe : "))
        print(f"Mot de passe généré : {generer_mot_de_passe(longueur)}")
    except ValueError as e:
        print(e)