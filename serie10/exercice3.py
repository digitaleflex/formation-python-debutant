import random

def jeu_devinette() -> None:
    """
    Simule un jeu de devinette où l'utilisateur doit trouver un nombre aléatoire.
    """
    nombre_aleatoire = random.randint(1, 100)
    tentatives = 0

    print("Bienvenue dans le jeu de devinette !")
    print("Devinez un nombre entre 1 et 100.")

    while True:
        try:
            devine = int(input("Votre essai : "))
            tentatives += 1
            if devine < nombre_aleatoire:
                print("Plus grand !")
            elif devine > nombre_aleatoire:
                print("Plus petit !")
            else:
                print(f"Félicitations ! Vous avez trouvé en {tentatives} tentative(s).")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Exemple d'utilisation
if __name__ == "__main__":
    jeu_devinette()