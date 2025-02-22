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

# Exemple d'utilisation
if __name__ == "__main__":
    print(maximum_de_trois(10, 20, 15))  # Résultat : 20