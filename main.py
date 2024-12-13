#Creating main display
from functions_grades import add_student, view_students, calculate_average, find_top_performer, update_student_grade, student_exists
#
def main():
    while True:
        print("\nStudent Grade Tracker:")
        print("1. Add student")
        print("2. View students and grades")
        print("3. Calculate averages")
        print("4. Find top performer")
        print("5. Update student grades")
        print("6. Exit")
# select choice
        choice=input("Enter your choice:")
#
        if choice=="1":
            name=input("Enter student's name:")
            if student_exists(name):
                print("The student '{name}' already exists.")
                continue
            grades = [float(input(f"Enter grade for subject {i + 1}: ")) for i in range(3)]
            add_student(name, grades)
            print(f"Student '{name}' added successfully with grades: {grades}.")
        
        elif choice == "2":
            students = view_students()
            if not students:
                print("No students available.")
            else:
                for name, grades in students.items():
                    print(f"{name}: {grades}")

        elif choice == "3":
            name = input("Enter student's name for average calculation: ")
            average = calculate_average(name)
            if average is not None:
                print(f"{name}'s average grade: {average:.2f}")
            else:
                print("Student not found.")
        
        elif choice == "4":
            top_performer = find_top_performer()
            if top_performer:
                name, average = top_performer
                print(f"Top performer: {name} with an average grade of {average:.2f}")
            else:
                print("No students available.")
        
        elif choice == "5":
            name = input("Enter student's name to update grade: ")
            if not student_exists(name):
                print("Student not found. Please enter a valid student name.")
                continue
            subject_index = int(input("Enter subject number to update (1, 2, or 3): ")) - 1
            if subject_index < 0 or subject_index > 2:
                print("Invalid subject number. Please enter 1, 2, or 3.")
                continue
            
            new_grade = float(input("Enter new grade: "))
            update_student_grade(name, subject_index, new_grade)
            print(f"{name}'s grade for subject {subject_index + 1} updated to {new_grade}.")
        
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()