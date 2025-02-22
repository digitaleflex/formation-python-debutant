import json

class Bibliotheque:
    def __init__(self, fichier: str):
        self.fichier = fichier
        self.charger_livres()

    def charger_livres(self):
        try:
            with open(self.fichier, "r") as f:
                self.livres = json.load(f)
        except FileNotFoundError:
            self.livres = []

    def sauvegarder_livres(self):
        with open(self.fichier, "w") as f:
            json.dump(self.livres, f, indent=4)

    def ajouter_livre(self, titre: str, auteur: str, genre: str):
        if any(livre["titre"] == titre for livre in self.livres):
            print("Ce livre existe déjà.")
            return
        self.livres.append({"titre": titre, "auteur": auteur, "genre": genre, "disponible": True})
        self.sauvegarder_livres()
        print(f"Livre '{titre}' ajouté avec succès.")

    def supprimer_livre(self, titre: str):
        for livre in self.livres:
            if livre["titre"] == titre:
                self.livres.remove(livre)
                self.sauvegarder_livres()
                print(f"Livre '{titre}' supprimé avec succès.")
                return
        print(f"Livre '{titre}' non trouvé.")

    def emprunter_livre(self, titre: str):
        for livre in self.livres:
            if livre["titre"] == titre and livre["disponible"]:
                livre["disponible"] = False
                self.sauvegarder_livres()
                print(f"Livre '{titre}' emprunté avec succès.")
                return
        print(f"Livre '{titre}' non disponible ou introuvable.")

    def retourner_livre(self, titre: str):
        for livre in self.livres:
            if livre["titre"] == titre and not livre["disponible"]:
                livre["disponible"] = True
                self.sauvegarder_livres()
                print(f"Livre '{titre}' retourné avec succès.")
                return
        print(f"Livre '{titre}' non emprunté ou introuvable.")

    def afficher_livres(self, genre: str = None):
        if genre:
            filtrer = [livre for livre in self.livres if livre["genre"] == genre]
        else:
            filtrer = self.livres

        if not filtrer:
            print("Aucun livre disponible.")
        else:
            for livre in filtrer:
                status = "Disponible" if livre["disponible"] else "Emprunté"
                print(f"{livre['titre']} par {livre['auteur']} - Genre: {livre['genre']} - {status}")

def menu_bibliotheque():
    bibliotheque = Bibliotheque("bibliotheque.json")
    while True:
        print("\nMenu :")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Afficher tous les livres")
        print("6. Afficher les livres par genre")
        print("7. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            genre = input("Genre du livre : ")
            bibliotheque.ajouter_livre(titre, auteur, genre)
        elif choix == "2":
            titre = input("Titre du livre à supprimer : ")
            bibliotheque.supprimer_livre(titre)
        elif choix == "3":
            titre = input("Titre du livre à emprunter : ")
            bibliotheque.emprunter_livre(titre)
        elif choix == "4":
            titre = input("Titre du livre à retourner : ")
            bibliotheque.retourner_livre(titre)
        elif choix == "5":
            bibliotheque.afficher_livres()
        elif choix == "6":
            genre = input("Afficher les livres du genre : ")
            bibliotheque.afficher_livres(genre)
        elif choix == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu_bibliotheque()