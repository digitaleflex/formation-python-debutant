# Demander un nombre à l'utilisateur
n = int(input("Entrez un nombre positif : "))

# Initialiser la variable pour stocker la somme
somme = 0

# Boucle for pour calculer la somme des nombres de 1 à n
for i in range(1, n + 1):  # Inclure n dans la somme
    somme += i

# Afficher le résultat
print(f"La somme des nombres de 1 à {n} est : {somme}")