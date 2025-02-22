# Demander un nombre à l'utilisateur
nombre = int(input("Entrez un nombre pour afficher sa table de multiplication : "))

# Boucle for pour afficher la table de multiplication
for i in range(1, 11):  # De 1 à 10
    print(f"{nombre} x {i} = {nombre * i}")