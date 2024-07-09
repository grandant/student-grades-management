import students


def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Calculate the average grade for a student")
        print("4. Display all students and their grades")
        print("5. Remove a student")
        print("6. Update a student's grade")
        print("7. Get a student's highest grade")
        print("8. Save student data to a file")
        print("9. Load student data from a file")
        print("10. Exit")

        choice = input("Waiting for an input: ")

        if choice == 1:
            name = input("Enter Student Name: ")
            students.add_student(name)
        elif choice == 2:
            name = input("Enter student\'s name: ")
            grades = input("Enter grades separated by comma: ")
            students.add_grade(name, grades)
        elif choice == 3:
            name = input("Enter student\'s name: ")
            students.calculate_average(name)
        elif choice == 4:
            students.display_students()
        elif choice == 5:
            name = input("Enter student\'s name: ")
            students.remove_student(name)
        elif choice == 6:
            name = input("Enter student\'s name: ")
            old_grade = int(input("Grade to change: "))
            new_grade = int(input("New grade: "))
            students.update_grade(name, old_grade, new_grade)
        elif choice == 7:
            name = input("Enter student\'s name: ")
            students.get_highest_grade(name)
        elif choice == 8:
            students.save_data()
        elif choice == 9:
            students.load_data()
        elif choice == 10:
            break
