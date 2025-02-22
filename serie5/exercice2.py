def est_pair(nombre: int) -> bool:
    """
    Vérifie si un nombre est pair.

    Args:
        nombre (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est pair, False sinon.
    """
    return nombre % 2 == 0

# Exemple d'utilisation
if __name__ == "__main__":
    print(est_pair(4))  # Résultat : True
    print(est_pair(7))  # Résultat : False