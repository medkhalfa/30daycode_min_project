#Creating all functions for the Student Grade Tracker
# Create a dictionary to store student's names and their grades
students_grades={}
#
# Add new student with grades
def add_student(name, grades):
    students_grades[name]=grades
#
# Return the dictionary of students
def view_students():
    return students_grades
#
# Calculate and return the averages
def calculate_average(name):
    grades = students_grades.get(name)
    if grades is not None:
        return sum(grades) / len(grades)
    return None
# Find and return the student with top grades
def find_top_performer():
    top_student = None
    top_average = 0
    for name, grades in students_grades.items():
        average=sum(grades) / len(grades)
        if average > top_average:
            top_average = average
            top_student = (name,average)
    return top_student
# Update the grade for a specific student
def update_student_grade(name,subject_index,new_grade):
    if name in students_grades and 0 <= subject_index <len(students_grades[name]):
            students_grades[name][subject_index]=new_grade
#
# Check if a student exists in the stored names
def student_exists(name):
    return name in students_grades