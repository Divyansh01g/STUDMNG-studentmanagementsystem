from result import students


def save_students():
    file = open("students.txt", "w")

    for name, data in students.items():
        marks = data["marks"]

        file.write(name + ",")
        file.write(str(marks[0]) + ",")
        file.write(str(marks[1]) + ",")
        file.write(str(marks[2]) + "\n")

    file.close()


def load_students():
    file = open("students.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) == 4:
            name = data[0]

            marks = [
                int(data[1]),
                int(data[2]),
                int(data[3])
            ]

            # Calculate the result again
            total, percentage, grade = calculate_result(marks)

            students[name] = {
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

    file.close()
