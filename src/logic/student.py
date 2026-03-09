from ..utils.utils import clearScreen, pause
from .id import generate_id
from ..middlewares.validation import get_validated_input, validate_name, validate_age, validate_ville, validate_filiere
from ..middlewares.file_operations import save_students_to_json



def createStudent(STUDENTS):
    clearScreen()

    print("=== AJOUTER UN ETUDIANT ===")
    print()


    name = get_validated_input("Nom: ", validate_name)
    while name is None:
        print("Le nom est requis.")
        name = get_validated_input("Nom: ", validate_name)
    

    age = get_validated_input("Age: ", validate_age)
    while age is None:
        print("L'âge est requis.")
        age = get_validated_input("Age: ", validate_age)

    ville = get_validated_input("Ville: ", validate_ville)
    while ville is None:
        print("La ville est requise.")
        ville = get_validated_input("Ville: ", validate_ville)

   

    filiere = get_validated_input("Filiere: ", validate_filiere)
    while filiere is None:
        print("La filiere est requise.")
        filiere = get_validated_input("Filiere: ", validate_filiere)

  
    student_id = generate_id(STUDENTS)

    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'ville': ville,
        'filiere': filiere,
        'notes': []
    }

    STUDENTS.append(student)

    
    success = save_students_to_json(STUDENTS)
    
    if success:
        print(f"\nEtudiant {name} ajoute avec succes!")
        print(f"ID genere: {student_id}")
    else:
        print(f"\nErreur lors de la sauvegarde de l'etudiant {name}.")

    pause()



