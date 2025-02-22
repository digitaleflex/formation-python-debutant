from typing import Any

def ajouter_element(dictionnaire: dict, cle: str, valeur: Any) -> None:
    """
    Ajoute un nouvel élément à un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire à modifier.
        cle (str): La clé du nouvel élément.
        valeur (any): La valeur associée à la clé.
    """
    dictionnaire[cle] = valeur

# Exemple d'utilisation
if __name__ == "__main__":
    personne = {"nom": "Charlie", "âge": 35, "ville": "Marseille"}
    ajouter_element(personne, "profession", "Ingénieur")
    print(personne)