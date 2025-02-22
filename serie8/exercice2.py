def lire_fichier(nom_fichier: str) -> str:
    """
    Lit le contenu d'un fichier texte.

    Args:
        nom_fichier (str): Le nom du fichier à lire.

    Returns:
        str: Le contenu du fichier.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return fichier.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    contenu = lire_fichier("fichier_demo.txt")
    print("Contenu du fichier :")
    print(contenu)