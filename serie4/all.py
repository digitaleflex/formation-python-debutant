def exercice_1():
    fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
    for fruit in fruits:
        print(fruit)

def exercice_2():
    nombres = []
    for i in range(5):
        while True:
            try:
                nombre = float(input(f"Entrez le nombre {i + 1} : "))
                nombres.append(nombre)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    print("Liste des nombres :", nombres)

def exercice_3():
    nombres = [42, 7, 19, 83, 5]
    if not nombres:
        print("La liste est vide.")
    else:
        plus_grand = max(nombres)
        plus_petit = min(nombres)
        print(f"Le plus grand nombre est : {plus_grand}")
        print(f"Le plus petit nombre est : {plus_petit}")

def exercice_4():
    elements = [1, 2, 3, 2, 4, 2, 5]
    element_recherche = int(input("Entrez l'élément à rechercher : "))
    occurrences = elements.count(element_recherche)
    print(f"L'élément {element_recherche} apparaît {occurrences} fois dans la liste.")

def exercice_5():
    liste = [10, 20, 30, 40, 50]
    liste_inverse = liste[::-1]
    print("Liste originale :", liste)
    print("Liste inversée :", liste_inverse)

# Appel des fonctions
if __name__ == "__main__":
    print("Exercice 1 :")
    exercice_1()
    print("\nExercice 2 :")
    exercice_2()
    print("\nExercice 3 :")
    exercice_3()
    print("\nExercice 4 :")
    exercice_4()
    print("\nExercice 5 :")
    exercice_5()