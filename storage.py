from result import students


def save_students():
    file = open("students.txt", "w")

    for name, data in students.items():
        marks = data["marks"]
        percentage = data["percentage"]
        grade = data["grade"]

        file.write(name + ",")
        file.write(str(marks[0]) + ",")
        file.write(str(marks[1]) + ",")
        file.write(str(marks[2]) + ",")
        file.write(str(percentage) + ",")
        file.write(grade + "\n")

    file.close()


def load_students():
    file = open("students.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) == 6:
            name = data[0]

            marks = [
                int(data[1]),
                int(data[2]),
                int(data[3])
            ]

            percentage = float(data[4])
            grade = data[5]

            students[name] = {
                "marks": marks,
                "percentage": percentage,
                "grade": grade
            }

    file.close()
