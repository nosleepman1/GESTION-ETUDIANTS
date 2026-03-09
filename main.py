from src.views.Home import home
from src.views.Searchs import SearchView
from src.utils.utils import clearScreen, pause
from src.logic.student import createStudent 
from src.logic.display import displayAllStudents
from src.logic.searchs import searchByName, searchByVille, searchByFiliere


from src.middlewares.file_operations import load_students_from_json




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
                if search_choice == 4:
                    break
                match search_choice:
                    case 1:
                        searchByName(students)
                    case 2:
                        searchByVille(students)
                    case 3:
                        searchByFiliere(students)
                    case _:
                        print("Option de recherche invalide.")
                                    
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
        