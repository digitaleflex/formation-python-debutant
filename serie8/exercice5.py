def copier_fichier(fichier_source: str, fichier_destination: str) -> None:
    """
    Copie le contenu d'un fichier vers un autre.

    Args:
        fichier_source (str): Le nom du fichier source.
        fichier_destination (str): Le nom du fichier de destination.

    Raises:
        FileNotFoundError: Si le fichier source n'existe pas.
    """
    try:
        with open(fichier_source, "r", encoding="utf-8") as source:
            with open(fichier_destination, "w", encoding="utf-8") as destination:
                destination.write(source.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier source '{fichier_source}' n'existe pas.")

# Exemple d'utilisation
if __name__ == "__main__":
    copier_fichier("fichier_demo.txt", "fichier_copie.txt")
    print("Le fichier a été copié avec succès.")