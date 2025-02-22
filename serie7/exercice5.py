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

# Exemple d'utilisation
if __name__ == "__main__":
    personne = {"nom": "Eve", "âge": 28, "ville": "Nice", "profession": "Développeur"}
    try:
        supprimer_element(personne, "profession")
        print("Élément supprimé avec succès.")
        print(personne)
    except KeyError as e:
        print(e)