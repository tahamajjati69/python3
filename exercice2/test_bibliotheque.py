from bibliotheque import Bibliotheque
from livre import Livre
from magazine import Magazine

biblio = Bibliotheque()
biblio.ajouter(Livre("1984", 1949, "George Orwell"))
biblio.ajouter(Magazine("Science & Vie", 2023, 456))
biblio.ajouter(Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"))

print("Affichage de tous les documents :")
biblio.afficher_tous()

print("\nRecherche par titre 'Petit' :")
for doc in biblio.rechercher("Petit"):
    doc.afficher()

print("\nDocuments récents :")
for doc in biblio.documents:
    if doc.est_recent(2022):
        doc.afficher()
