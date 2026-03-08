import json
import os

DATA_FILE = "src/database/students.json"

def save_students_to_json(students):
    
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(students, f, indent=2)
        return True,
    except:
        return False, 

def load_students_from_json():
    
    try:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, 'r') as f:
            students = json.load(f)
        return students
    except:
        print("Erreur lors du chargement des données...........")
        return []