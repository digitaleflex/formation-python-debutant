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

# Exemple d'utilisation
if __name__ == "__main__":
    personne = {"nom": "David", "âge": 40, "ville": "Toulouse"}
    cle_a_verifier = "profession"
    if verifier_cle_existe(personne, cle_a_verifier):
        print(f"La clé '{cle_a_verifier}' existe dans le dictionnaire.")
    else:
        print(f"La clé '{cle_a_verifier}' n'existe pas dans le dictionnaire.")