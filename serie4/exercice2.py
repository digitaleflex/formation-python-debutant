# Initialisation de la liste vide
nombres = []

# Boucle pour demander 5 nombres à l'utilisateur
for i in range(5):
    while True:
        try:
            nombre = float(input(f"Entrez le nombre {i + 1} : "))
            nombres.append(nombre)
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

print("Liste des nombres :", nombres)