def ecrire_dans_fichier(nom_fichier: str, message: str) -> None:
    """
    Crée un fichier texte et écrit un message dedans.

    Args:
        nom_fichier (str): Le nom du fichier à créer.
        message (str): Le message à écrire dans le fichier.
    """
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(message)


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


# Tests des fonctions
if __name__ == "__main__":
    # Exercice 1
    ecrire_dans_fichier("fichier_demo.txt", "Bonjour, ceci est un message de test.")

    # Exercice 2
    contenu = lire_fichier("fichier_demo.txt")
    print("Contenu du fichier :")
    print(contenu)

    # Exercice 3
    ajouter_ligne("fichier_demo.txt", "Ceci est une nouvelle ligne ajoutée.")

    # Exercice 4
    nombre_lignes = compter_lignes("fichier_demo.txt")
    print(f"Nombre de lignes dans le fichier : {nombre_lignes}")

    # Exercice 5
    copier_fichier("fichier_demo.txt", "fichier_copie.txt")
    print("Le fichier a été copié avec succès.")