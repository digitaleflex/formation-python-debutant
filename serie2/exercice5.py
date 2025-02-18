# Demander un nombre à l'utilisateur
nombre = int(input("Entrez un nombre : "))

# Vérifier si le nombre est un multiple de 3, de 5, ou des deux
if nombre % 3 == 0 and nombre % 5 == 0:  # Multiple de 3 ET de 5
    print(f"Le nombre {nombre} est un multiple de 3 et de 5.")
elif nombre % 3 == 0:  # Multiple de 3 seulement
    print(f"Le nombre {nombre} est un multiple de 3.")
elif nombre % 5 == 0:  # Multiple de 5 seulement
    print(f"Le nombre {nombre} est un multiple de 5.")
else:  # Pas un multiple de 3 ni de 5
    print(f"Le nombre {nombre} n'est ni un multiple de 3 ni de 5.")