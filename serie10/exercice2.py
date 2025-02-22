def addition(a: float, b: float) -> float:
    """Réalise l'addition de deux nombres."""
    return a + b

def soustraction(a: float, b: float) -> float:
    """Réalise la soustraction de deux nombres."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Réalise la multiplication de deux nombres."""
    return a * b

def division(a: float, b: float) -> float:
    """
    Réalise la division de deux nombres.

    Raises:
        ZeroDivisionError: Si le diviseur est zéro.
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible.")
    return a / b

def calculatrice() -> None:
    """
    Affiche un menu pour effectuer des opérations mathématiques simples.
    """
    operations = {
        "1": ("Addition", addition),
        "2": ("Soustraction", soustraction),
        "3": ("Multiplication", multiplication),
        "4": ("Division", division),
    }

    print("Bienvenue dans la calculatrice !")
    for key, (operation_name, _) in operations.items():
        print(f"{key}. {operation_name}")

    choix = input("Choisissez une opération (1-4) : ")
    if choix not in operations:
        print("Opération invalide.")
        return

    operation_name, operation_func = operations[choix]
    try:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        resultat = operation_func(a, b)
        print(f"Résultat de {operation_name} : {resultat}")
    except ValueError:
        print("Veuillez entrer des nombres valides.")
    except ZeroDivisionError as e:
        print(e)

# Exemple d'utilisation
if __name__ == "__main__":
    calculatrice()