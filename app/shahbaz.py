
import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully!")

def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)

def search_student(students):
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:", student)
            return

    print("Student not found!")

def delete_student(students):
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted!")
            return

    print("Student not found!")

def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
