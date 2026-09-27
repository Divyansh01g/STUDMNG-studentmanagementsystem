students = {}

def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def add_student(name, marks):
    total, percentage, grade = calculate_result(marks)

    students[name] = {
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }


def search_student(name):
    return students.get(name)


def view_students():
    return students
