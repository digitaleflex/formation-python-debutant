# Demander un nombre à l'utilisateur
nombre = float(input("Entrez un nombre : "))

# Vérifier si le nombre est positif, négatif ou nul
if nombre > 0:  # Si le nombre est strictement supérieur à 0
    print(f"Le nombre {nombre} est positif.")
elif nombre < 0:  # Si le nombre est strictement inférieur à 0
    print(f"Le nombre {nombre} est négatif.")
else:  # Si le nombre est égal à 0
    print(f"Le nombre {nombre} est nul.")