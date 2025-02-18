# Bonne pratique : Convertir explicitement les entrées utilisateur en types appropriés (float ou int).
try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    somme = nombre1 + nombre2
    print(f"La somme de {nombre1} et {nombre2} est : {somme}")
except ValueError:
    print("Veuillez entrer des nombres valides.")