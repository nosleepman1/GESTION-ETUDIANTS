from .display import displayStudent
from src.utils.utils import clearScreen, pause


def searchByName(STUDENTS):
    name = input("Entrez le nom de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['name'].lower() == name]
    
    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) avec le nom '{name}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve avec le nom '{name}'.")
    pause()
        
        
        
def searchByVille(STUDENTS):
    ville = input("Entrez la ville de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['ville'].lower() == ville]
    
    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) dans la ville '{ville}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve dans la ville '{ville}'.")
    pause()



def searchByFiliere(STUDENTS):
    filiere = input("Entrez la filiere de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['filiere'].lower() == filiere]

    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) dans la filiere '{filiere}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve dans la filiere '{filiere}'.")
    pause()


def searchById(STUDENTS):
    student_id = int(input("Entrez l'ID de l'etudiant a rechercher: "))
    RESULT = [student for student in STUDENTS if student['id'] == student_id]
    
    return RESULT
