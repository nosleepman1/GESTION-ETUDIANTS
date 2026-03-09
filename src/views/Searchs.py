

def SearchView():
    from ..utils.utils import clearScreen
    clearScreen()
    print("=== Rechercher un étudiant ===")
    print("1. Par nom")
    print("2. Par ville")
    print("3. Par filière")
    print("4. Retour au menu principal")
    choix = int(input("Veuillez choisir une option de recherche: "))
    return choix