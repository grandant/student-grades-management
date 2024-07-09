students = {}


def add_student(name):
    name = input("Enter Student Name: ")
    students[name] = []


def add_grade(name, grade):
    name = input("Enter student\'s name: ")
    grades = input("Enter grades separated by comma: ")
    grades_list = grades.join(', ')
    students[name] = grades_list


def calculate_average(name):
    name = input("Enter student\'s name: ")
    grades = students[name]
    sum_grade = 0
    for grade in grades:
        sum_grade += grade

    avr_grade = sum_grade / len(grades)
    print(f"The average grade of student {name} is: {avr_grade}")

def display_students():
    pass


def remove_student(name):
    pass


def update_grade(name, old_grade, new_grade):
    pass


def get_highest_grade(name):
    pass


def save_data(filename='data/students_data.txt'):
    pass


def load_data(filename='data/students_data.txt'):
    pass
