# storage.py

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
    file = open("students.txt", "a+")
    file.seek(0)

    for line in file:
        data = line.strip().split(",")

        if len(data) == 4:
            name = data[0]

            marks = [
                int(data[1]),
                int(data[2]),
                int(data[3])
            ]

            students[name] = {
                "marks": marks
            }

    file.close()
