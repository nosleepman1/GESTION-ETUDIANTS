from src.views.Home import home
from src.utils.utils import clearScreen, pause




while True:
    choix = home()
    
    match choix:
        case 1:
            print("Ajouter un étudiant")
            pause()
        case 2:
            print("Afficher les étudiants")
            pause()
        case 3:
            print("Rechercher un étudiant")
            pause()
        case 4:
            print("Ajouter une note")
            pause()
        case 5:
            print("Afficher les statistiques")
            pause()
        case 6:
            print("Exporter vers CSV")
            pause()
        case 7:
            print("Supprimer un étudiant")
            pause()
        case 8:
            print("Modifier un étudiant")
            pause()
        case 9:
            print("Quitter")
            break
        