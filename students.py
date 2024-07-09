students = {}


def add_student(name):
    pass


def add_grade(name, grade):
    pass


def calculate_average(name):
    pass


def display_students():
    pass


def remove_student(name):
    name = input("Enter a student name: ")
    if name in students:
        del students[name]
        print(f"The student {name} was removed.")
    else:
        print("The student not found.")


def update_grade(name, old_grade, new_grade):
    pass


def get_highest_grade(name):
    pass


def save_data(filename='data/students_data.txt'):
    pass


def load_data(filename='data/students_data.txt'):
    pass
