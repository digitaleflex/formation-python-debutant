def compter_lignes(nom_fichier: str) -> int:
    """
    Compte le nombre de lignes dans un fichier texte.

    Args:
        nom_fichier (str): Le nom du fichier à analyser.

    Returns:
        int: Le nombre de lignes dans le fichier.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return sum(1 for _ in fichier)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    nombre_lignes = compter_lignes("fichier_demo.txt")
    print(f"Nombre de lignes dans le fichier : {nombre_lignes}")