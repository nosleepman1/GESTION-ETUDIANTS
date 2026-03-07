

def pause():
    input("Appuyez sur une touche pour continuer...")
    
def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')