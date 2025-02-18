# Demander à l'utilisateur de saisir un nombre
nombre = int(input("Entrez un nombre : "))

# Utiliser l'opérateur modulo (%) pour vérifier si le nombre est pair ou impair
if nombre % 2 == 0:  # Si le reste de la division par 2 est 0, le nombre est pair
    print(f"Le nombre {nombre} est pair.")
else:  # Sinon, le nombre est impair
    print(f"Le nombre {nombre} est impair.")