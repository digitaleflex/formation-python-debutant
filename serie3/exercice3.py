import random  # Importer le module random pour générer un nombre aléatoire

# Générer un nombre aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)

# Initialiser la variable pour stocker la réponse de l'utilisateur
devine = None

# Boucle while pour demander à l'utilisateur de deviner le nombre
while devine != nombre_aleatoire:
    try:
        devine = int(input("Devinez un nombre entre 1 et 10 : "))
        if devine < nombre_aleatoire:
            print("Trop petit !")
        elif devine > nombre_aleatoire:
            print("Trop grand !")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

print("Bravo ! Vous avez trouvé le nombre.")