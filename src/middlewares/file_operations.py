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



def save_students_to_csv(STUDENTS):
    try:
        with open('students.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age', 'ville', 'filiere'])
            writer.writeheader()
            writer.writerows(STUDENTS)
        return True
    except Exception as e:
        print(f"Erreur lors de l'exportation vers CSV: {e}")
        return False


def load_students_from_csv(STUDENTS):
    try:
        with open('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                STUDENTS.append(row)
        return True
    except Exception as e:
        print(f"Erreur lors de l'importation depuis CSV: {e}")
        return False