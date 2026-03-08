from os import system


def home():
    system('cls')
     
    print("===========GESTION DES ETUDIANTS===========")
    print("1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Rechercher un étudiant")
    print("4. Ajouter une note")
    print("5. Afficher les statistiques")
    print("6. Exporter vers CSV")
    print("7. Supprimer un étudiant")   
    print("8. Modifier un étudiant")
    print("9. Quitter")
    
    choix = int(input("Veuillez choisir une option: "))
    return choix