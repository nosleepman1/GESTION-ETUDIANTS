def validate_name(name):   
    try:
        if not name.strip():
            return False, "Le nom ne peut pas être vide"
        
        if len(name.strip()) < 2:
            return False, "Le nom doit contenir au moins 2 caractères"
      
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False, "Le nom ne peut contenir que des lettres et des espaces"
        return True, name
    except:
        return False, "Erreur de validation du nom"


def validate_age(age_str):
    try:
        age = int(age_str)
        
        if age < 16 or age > 100:
            return False, "L'âge doit être entre 16 et 100 ans"
        
        return True, age
    
    except ValueError:
        return False, "L'âge doit être un nombre entier"


def validate_ville(ville):
   
    try:
        if not ville.strip():
            return False, "La ville ne peut pas être vide"
 
        for char in ville:
            
            if not (char.isalpha() or char.isspace()):
                return False, "La ville ne peut contenir que des lettres et des espaces"      
            
        return True, ville
   
    except:
        return False, "Erreur de validation de la ville"


def validate_filiere(filiere):
    
    try:
        if not filiere.strip():
            return False, "La filière ne peut pas être vide"
        
        for char in filiere:
            
            if not (char.isalpha() or char.isspace()):
                return False, "La filière ne peut contenir que des lettres et des espaces"
            
        return True, filiere
    except:
        return False, "Erreur de validation de la filière"
    

def validate_grade(grade):
    try:
        grade_value = int(grade)
        
        if grade_value < 0 or grade_value > 20:
            return False, "La note doit être entre 0 et 20"
        
        return True, grade_value
    
    except ValueError:
        return False, "La note doit être un nombre valide"


def get_validated_input(text, validator):
   
    while True:
        user_input = input(text)
        
        is_valid, result = validator(user_input)
        
        if is_valid:
            return result
        else:
            print(f"Erreur: {result}")
            

