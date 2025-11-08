from livre import Livre
from magazine import Magazine

class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, doc):
        self.documents.append(doc)

    def afficher_tous(self):
        for doc in self.documents:
            doc.afficher()

    def rechercher(self, titre_fragment):
        return [doc for doc in self.documents if titre_fragment.lower() in doc.titre.lower()]
