def factorielle(nombre: int) -> int:
    """
    Calcule la factorielle d'un nombre.

    Args:
        nombre (int): Le nombre dont on veut calculer la factorielle.
                      Doit être un entier positif ou nul.

    Returns:
        int: La factorielle du nombre.

    Raises:
        ValueError: Si le nombre est négatif.
    """
    if nombre < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    result = 1
    for i in range(1, nombre + 1):
        result *= i
    return result

# Exemple d'utilisation
if __name__ == "__main__":
    print(factorielle(5))  # Résultat : 120