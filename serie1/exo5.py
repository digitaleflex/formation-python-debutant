# Bonne pratique : Valider les entrées utilisateur et gérer les erreurs.
try:
    longueur = float(input("Entrez la longueur du rectangle : "))
    largeur = float(input("Entrez la largeur du rectangle : "))

    if longueur <= 0 or largeur <= 0:
        print("Les dimensions doivent être positives.")
    else:
        aire = longueur * largeur
        print(f"L'aire du rectangle est : {aire}")
except ValueError:
    print("Veuillez entrer des valeurs numériques valides.")