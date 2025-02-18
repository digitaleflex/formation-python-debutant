# Bonne pratique : Utiliser des fonctions natives comme str() et int() pour les conversions.
entier = 42
chaine = str(entier)  # Conversion d'un entier en chaîne
print(f"L'entier {entier} converti en chaîne : {chaine}")

chaine_nombre = "123"
nouvel_entier = int(chaine_nombre)  # Conversion d'une chaîne en entier
print(f"La chaîne '{chaine_nombre}' convertie en entier : {nouvel_entier}")