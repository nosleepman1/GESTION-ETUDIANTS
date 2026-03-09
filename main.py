from logic.searchs import searchByName
from src.views.Home import home
from src.utils.utils import clearScreen, pause
from src.logic.student import createStudent, displayAllStudents
from src.middlewares.file_operations import load_students_from_json
from views.Searchs import SearchView




# Load students from JSON at startup
students = load_students_from_json()

while True:
    choix = home()

    match choix:
        case 1:
            createStudent(students)
        case 2:
            displayAllStudents(students)
        case 3:
            while True:
                search_choice = SearchView()
                match search_choice:
                    case 1:
                        searchByName(students)
                    case 2:
                        print("Recherche par ville - Fonctionnalité à implémenter")
                        pause()
                    case 3:
                        print("Recherche par filière - Fonctionnalité à implémenter")
                        pause()
                    case 4:
                        break
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
        