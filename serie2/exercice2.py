# Demander l'âge de la personne
age = int(input("Entrez votre âge : "))

# Vérifier si la personne est majeure (>= 18) ou mineure (< 18)
if age >= 18:
    print("Vous êtes majeur(e).")
else:
    print("Vous êtes mineur(e).")