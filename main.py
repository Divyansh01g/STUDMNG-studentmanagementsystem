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
        m1 = int(input("Subject 1 Marks: "))
        m2 = int(input("Subject 2 Marks: "))
        m3 = int(input("Subject 3 Marks: "))
        marks = [m1, m2, m3]

        add_student(name, marks)
        save_students()
        print("Student added successfully!")


    
    elif choice == "2":

        name = input("Enter student name: ")

        result = search_student(name)
        if result:
            print("\nName:", name)
            print("Marks:", result["marks"])
            print("Total:", result["total"])
            print("Percentage:", result["percentage"])
            print("Grade:", result["grade"])
        else:
            print("Student not found.")

    elif choice == "3":
        data = view_students()

        if len(data) == 0:
            print("No records available.")
        else:
            for name, result in data.items():
                print("\nName:", name)
                print("Marks:", result["marks"])
                print("Total:", result["total"])
                print("Percentage:", result["percentage"])
                print("Grade:", result["grade"])

    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
