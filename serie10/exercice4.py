def metres_en_kilometres(metres: float) -> float:
    """Convertit des mètres en kilomètres."""
    return metres / 1000

def celsius_en_fahrenheit(celsius: float) -> float:
    """Convertit des degrés Celsius en Fahrenheit."""
    return (celsius * 9/5) + 32

def convertisseur_unites() -> None:
    """
    Affiche un menu pour convertir des unités.
    """
    conversions = {
        "1": ("Mètres en Kilomètres", metres_en_kilometres),
        "2": ("Celsius en Fahrenheit", celsius_en_fahrenheit),
    }

    print("Bienvenue dans le convertisseur d'unités !")
    for key, (conversion_name, _) in conversions.items():
        print(f"{key}. {conversion_name}")

    choix = input("Choisissez une conversion (1-2) : ")
    if choix not in conversions:
        print("Conversion invalide.")
        return

    conversion_name, conversion_func = conversions[choix]
    try:
        valeur = float(input("Entrez la valeur à convertir : "))
        resultat = conversion_func(valeur)
        print(f"Résultat de {conversion_name} : {resultat}")
    except ValueError:
        print("Veuillez entrer une valeur numérique valide.")

# Exemple d'utilisation
if __name__ == "__main__":
    convertisseur_unites()