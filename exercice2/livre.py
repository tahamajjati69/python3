from document import Document

class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")
