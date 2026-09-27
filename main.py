from result import add_student, search_student, view_students
from storage import load_students, save_students

load_students()

while True:
    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        mark1 = int(input("Enter marks for Subject 1: "))
        mark2 = int(input("Enter marks for Subject 2: "))
        mark3 = int(input("Enter marks for Subject 3: "))

        marks = [mark1, mark2, mark3]

        add_student(name, marks)
        save_students()

        print("Student result saved successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        result = search_student(name)

        if result:
            print("\nName:", name)
            print("Marks:", result["marks"])

            if "percentage" in result:
                print("Percentage:", result["percentage"])
                print("Grade:", result["grade"])
            else:
                print("Percentage and grade will be calculated after saving again.")
        else:
            print("Student not found.")

    elif choice == "3":
        data = view_students()

        if len(data) == 0:
            print("No student records found.")
        else:
            print("\n----- Student Records -----")

            for name, result in data.items():
                print("\nName:", name)
                print("Marks:", result["marks"])

                if "percentage" in result:
                    print("Percentage:", result["percentage"])
                    print("Grade:", result["grade"])

    elif choice == "4":
        print("Thank you for using the Student Result Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
