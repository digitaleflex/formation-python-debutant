def carre(nombre: float) -> float:
    """
    Calcule le carré d'un nombre.

    Args:
        nombre (float): Le nombre dont on veut calculer le carré.

    Returns:
        float: Le carré du nombre.
    """
    return nombre ** 2


def est_pair(nombre: int) -> bool:
    """
    Vérifie si un nombre est pair.

    Args:
        nombre (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est pair, False sinon.
    """
    return nombre % 2 == 0


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


def saluer(prenom: str) -> None:
    """
    Affiche un message de salutation avec le prénom donné.

    Args:
        prenom (str): Le prénom de la personne à saluer.
    """
    print(f"Bonjour, {prenom} !")


def maximum_de_trois(a: float, b: float, c: float) -> float:
    """
    Retourne le maximum de trois nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.
        c (float): Troisième nombre.

    Returns:
        float: Le plus grand des trois nombres.
    """
    return max(a, b, c)


# Tests des fonctions
if __name__ == "__main__":
    print(carre(5))  # Résultat : 25
    print(est_pair(4))  # Résultat : True
    print(est_pair(7))  # Résultat : False
    print(factorielle(5))  # Résultat : 120
    saluer("Alice")  # Résultat : Bonjour, Alice !
    print(maximum_de_trois(10, 20, 15))  # Résultat : 20