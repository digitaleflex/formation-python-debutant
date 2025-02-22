def ecrire_dans_fichier(nom_fichier: str, message: str) -> None:
    """
    Crée un fichier texte et écrit un message dedans.

    Args:
        nom_fichier (str): Le nom du fichier à créer.
        message (str): Le message à écrire dans le fichier.
    """
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(message)

# Exemple d'utilisation
if __name__ == "__main__":
    ecrire_dans_fichier("fichier_demo.txt", "Bonjour, ceci est un message de test.")