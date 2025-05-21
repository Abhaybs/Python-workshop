import os
import csv


folder_path = os.path.join(os.path.expanduser("~"), "Documents", "students_data")
file_path = os.path.join(folder_path, "students.csv")

def create_file():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")

    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Course"])
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")
def write_file(name, age, course):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, course])
    print(f"Data written: {name}, {age}, {course}")

def read_file():
    if not os.path.exists(file_path):
        print("File doesn't exist yet.")
        return
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def search_student(search_name):
    found = False
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0].lower() == search_name.lower():
                print("Student Found:", ', '.join(row))
                found = True
                break
    if not found:
        print("Student not found.")

def clear_data():
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Course"])
    print("All data cleared.")

def validate_input():
    name = input("Enter name: ").strip()
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Age must be a number.")
    course = input("Enter course: ").strip()
    return name, age, course

if __name__ == "__main__":
    create_file()
    while True:
        print("\nChoose an option:")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by name")
        print("4. Clear all records")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name, age, course = validate_input()
            write_file(name, age, course)
        elif choice == "2":
            read_file()
        elif choice == "3":
            search_name = input("Enter name to search: ")
            search_student(search_name)
        elif choice == "4":
            confirm = input("Are you sure you want to delete all records? (yes/no): ")
            if confirm.lower() == "yes":
                clear_data()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")