


def generate_id(students):
    if not students:
        return 1
    else:
        return max(student['id'] for student in students) + 1
    
