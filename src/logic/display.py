from ..utils.utils import clearScreen, pause




def displayStudent(student):
    
    print("=== FICHE ETUDIANT ===")
    print(f"ID: {student['id']}")
    print(f"Nom: {student['name']}")
    print(f"Age: {student['age']} ans")
    print(f"Ville: {student['ville']}")
    print(f"Filiere: {student['filiere']}")

    if student['notes']:
        print(f"Nombre de notes: {len(student['notes'])}")
        try:
            moyenne = sum(student['notes']) / len(student['notes'])
            print(f"Moyenne: {moyenne:.2f}/20")
        except:
            print("Erreur calcul moyenne")
    else:
        print("Aucune note enregistree")

    print("======================")




def displayAllStudents(students):
    
    clearScreen()

    if not students:
        print("=== AUCUN ETUDIANT ENREGISTRE ===")
        pause()
        return

    print("=== LISTE DES ETUDIANTS ===")
    print()

    for i, student in enumerate(students, 1):
        print(f"Etudiant {i}: ")
        print(f"  ID: {student['id']} | Nom: {student['name']} | Age: {student['age']} | Ville: {student['ville']} | Filiere: {student['filiere']}")
        if student['notes']:
            try:
                moyenne = sum(student['notes']) / len(student['notes'])
                print(f"  Notes: {len(student['notes'])} | Moyenne: {moyenne:.2f}/20")
            except:
                print(f"  Notes: {len(student['notes'])} | Erreur moyenne")
        else:
            print("  Aucune note")
        print("  -------------------")

    print()
    print(f"Total: {len(students)} etudiant(s)")
    pause()
    
    
