from .display import displayStudent


def searchByName(STUDENTS):
    name = input("Entrez le nom de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['name'].lower() == name]
    
    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) avec le nom '{name}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve avec le nom '{name}'.")
        
        
        
def searchByVille(STUDENTS):
    ville = input("Entrez la ville de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['ville'].lower() == ville]
    
    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) dans la ville '{ville}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve dans la ville '{ville}'.")



def searchByFiliere(STUDENTS):
    filiere = input("Entrez la filiere de l'etudiant a rechercher: ").lower()
    RESULTS = [student for student in STUDENTS if student['filiere'].lower() == filiere]

    if RESULTS:
        print(f"{len(RESULTS)} etudiant(s) trouve(s) dans la filiere '{filiere}':")
        for student in RESULTS:
            displayStudent(student)
    else:
        print(f"Aucun etudiant trouve dans la filiere '{filiere}'.")