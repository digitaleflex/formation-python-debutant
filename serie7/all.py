def creer_personne(nom: str, age: int, ville: str) -> dict:
    """
    Crée un dictionnaire contenant des informations sur une personne.

    Args:
        nom (str): Le nom de la personne.
        age (int): L'âge de la personne.
        ville (str): La ville où réside la personne.

    Returns:
        dict: Un dictionnaire contenant les informations.
    """
    return {"nom": nom, "âge": age, "ville": ville}


def afficher_elements(dictionnaire: dict) -> None:
    """
    Affiche les clés et les valeurs d'un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire à afficher.
    """
    print("Clés : ", list(dictionnaire.keys()))
    print("Valeurs : ", list(dictionnaire.values()))


def ajouter_element(dictionnaire: dict, cle: str, valeur: any) -> None:
    """
    Ajoute un nouvel élément à un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire à modifier.
        cle (str): La clé du nouvel élément.
        valeur (any): La valeur associée à la clé.
    """
    dictionnaire[cle] = valeur


def verifier_cle_existe(dictionnaire: dict, cle: str) -> bool:
    """
    Vérifie si une clé existe dans un dictionnaire.

    Args:
        dictionnaire (dict): Le dictionnaire à vérifier.
        cle (str): La clé à rechercher.

    Returns:
        bool: True si la clé existe, False sinon.
    """
    return cle in dictionnaire


def supprimer_element(dictionnaire: dict, cle: str) -> None:
    """
    Supprime un élément d'un dictionnaire si la clé existe.

    Args:
        dictionnaire (dict): Le dictionnaire à modifier.
        cle (str): La clé de l'élément à supprimer.

    Raises:
        KeyError: Si la clé n'existe pas dans le dictionnaire.
    """
    if cle in dictionnaire:
        del dictionnaire[cle]
    else:
        raise KeyError(f"La clé '{cle}' n'existe pas dans le dictionnaire.")


# Tests des fonctions
if __name__ == "__main__":
    # Exercice 1
    personne = creer_personne("Alice", 30, "Paris")
    print("Personne créée :", personne)

    # Exercice 2
    afficher_elements(personne)

    # Exercice 3
    ajouter_element(personne, "profession", "Ingénieur")
    print("Après ajout d'un élément :", personne)

    # Exercice 4
    cle_a_verifier = "profession"
    if verifier_cle_existe(personne, cle_a_verifier):
        print(f"La clé '{cle_a_verifier}' existe dans le dictionnaire.")
    else:
        print(f"La clé '{cle_a_verifier}' n'existe pas dans le dictionnaire.")

    # Exercice 5
    try:
        supprimer_element(personne, "profession")
        print("Après suppression d'un élément :", personne)
    except KeyError as e:
        print(e)