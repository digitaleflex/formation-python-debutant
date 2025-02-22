def ajouter_ligne(nom_fichier: str, ligne: str) -> None:
    """
    Ajoute une ligne de texte à un fichier existant.

    Args:
        nom_fichier (str): Le nom du fichier à modifier.
        ligne (str): La ligne à ajouter.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    try:
        with open(nom_fichier, "a", encoding="utf-8") as fichier:
            fichier.write(ligne + "\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    ajouter_ligne("fichier_demo.txt", "Ceci est une nouvelle ligne ajoutée.")