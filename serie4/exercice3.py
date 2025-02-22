# Liste de nombres (peut être remplacée par une liste fournie par l'utilisateur)
nombres = [42, 7, 19, 83, 5]

if not nombres:  # Vérifier si la liste est vide
    print("La liste est vide.")
else:
    plus_grand = max(nombres)  # Utiliser la fonction built-in max()
    plus_petit = min(nombres)  # Utiliser la fonction built-in min()

    print(f"Le plus grand nombre est : {plus_grand}")
    print(f"Le plus petit nombre est : {plus_petit}")