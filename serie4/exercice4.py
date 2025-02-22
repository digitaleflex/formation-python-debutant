# Liste d'exemple
elements = [1, 2, 3, 2, 4, 2, 5]

# Demander à l'utilisateur l'élément à rechercher
element_recherche = int(input("Entrez l'élément à rechercher : "))

# Compter les occurrences avec la méthode count()
occurrences = elements.count(element_recherche)

print(f"L'élément {element_recherche} apparaît {occurrences} fois dans la liste.")