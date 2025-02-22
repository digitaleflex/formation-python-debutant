class GestionnaireContacts:
    """
    Classe pour gérer les contacts utilisant un dictionnaire.
    """

    def __init__(self) -> None:
        """Initialise un gestionnaire de contacts vide."""
        self.contacts: dict[str, str] = {}

    def ajouter_contact(self, nom: str, telephone: str) -> None:
        """Ajoute un contact au gestionnaire."""
        self.contacts[nom] = telephone
        print(f"Contact '{nom}' ajouté avec succès.")

    def supprimer_contact(self, nom: str) -> None:
        """
        Supprime un contact du gestionnaire.

        Raises:
            KeyError: Si le contact n'existe pas.
        """
        if nom in self.contacts:
            del self.contacts[nom]
            print(f"Contact '{nom}' supprimé avec succès.")
        else:
            raise KeyError(f"Le contact '{nom}' n'existe pas.")

    def afficher_contacts(self) -> None:
        """Affiche tous les contacts."""
        if not self.contacts:
            print("Aucun contact disponible.")
        else:
            print("Liste des contacts :")
            for nom, telephone in self.contacts.items():
                print(f"{nom} : {telephone}")

# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireContacts()
    gestionnaire.ajouter_contact("Alice", "123-456-7890")
    gestionnaire.ajouter_contact("Bob", "987-654-3210")
    gestionnaire.afficher_contacts()

    try:
        gestionnaire.supprimer_contact("Alice")
        gestionnaire.afficher_contacts()
    except KeyError as e:
        print(e)