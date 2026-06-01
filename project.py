class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = []


def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student = Student(name, marks)
    students.append(student)
    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student.name}, Marks: {student.marks}")


def search_student():
    search_name = input("Enter name to search: ")

    for student in students:
        if student.name.lower() == search_name.lower():
            print(f"Found: {student.name}, Marks: {student.marks}")
            return

    print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice")