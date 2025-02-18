# Définir un mot de passe prédéfini
mot_de_passe_correct = "secret123"

# Demander à l'utilisateur de saisir un mot de passe
mot_de_passe_utilisateur = input("Entrez votre mot de passe : ")

# Vérifier si le mot de passe entré correspond au mot de passe prédéfini
if mot_de_passe_utilisateur == mot_de_passe_correct:
    print("Mot de passe correct. Accès autorisé.")
else:
    print("Mot de passe incorrect. Accès refusé.")