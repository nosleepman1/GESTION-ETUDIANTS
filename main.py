from src.logic.searchs import searchByName
from src.views.Home import home
from src.views.Searchs import SearchView
from src.utils.utils import clearScreen, pause
from src.logic.student import createStudent, addGrade, exportToCSV, editStudent, deleteStudent, importFromCSV
from src.logic.display import displayAllStudents
from src.logic.searchs import searchByName, searchByVille, searchByFiliere




from src.middlewares.file_operations import load_students_from_json
from src.views.Searchs import SearchView




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
                        searchByVille(students)
                    case 3:
                        searchByFiliere(students)
                    case 4:
                        break
            pause()
        case 4:
            addGrade(students)
            pause()
        case 5:
            print("Afficher les statistiques")
            pause()
        case 6:
            exportToCSV(students)
            pause()
        case 7:
            deleteStudent(students) 
            pause()
        case 8:
            editStudent(students)
            pause()
        case 9:
            print("Quitter")
            break
        