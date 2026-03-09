from src.views.Home import home
from src.utils.utils import clearScreen, pause
from src.logic.student import createStudent, displayAllStudents
from src.middlewares.file_operations import load_students_from_json




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
        