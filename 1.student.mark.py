def input_students_information():
    a = input("Enter student ID: ")
    b = input("Enter student name: ")
    c = input("Enter student's DoB: ")
    return {'id': a, 'name': b, 'dob': c, 'marks': {}}

def input_number_of_courses():
    e = int(input("Enter the number of courses: "))
    return e

def input_course_information():
    f = input("Enter course name: ")
    h = input("Enter course ID: ")
    return {'id': h, 'name': f}

def count_number_of_courses(courses):
    Courses_count = len(courses)
    print(f"Number of courses: {Courses_count}")

    if Courses_count > 0:
        print("Courses inputted:")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")
    else:
        print("No courses have been inputted yet.")

def mark(students, courses):
    course_id = input("Enter course ID for which you want to enter marks: ")
    student_id = input("Enter student ID for whom you want to enter marks: ")

    found_student = next((student for student in students if student['id'] == student_id), None)
    found_course = next((course for course in courses if course['id'] == course_id), None)

    if found_student and found_course:
        marks = float(input(f"Enter marks for student {found_student['name']} in {found_course['name']}: "))
        found_student['marks'][found_course['id']] = marks
    else:
        print("Student or course not found.")

def input_number_of_students():
    students_count = 0

    while True:
        try:
            x = int(input("Enter the number of students in the class: "))
            if x > 0:
                print("The number of students in the class is: ", x)
                students_count = x
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return students_count

def update_number_of_students(class_count, new_students):
    return class_count + new_students


def list_students(students):
    if students:
        print("List of Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}")
    else:
        print("No students have been inputted yet.")

def show_student_marks(students, courses):
    student_id = input("Enter student ID for whom you want to show marks: ")
    course_id = input("Enter course ID for which you want to show marks: ")

    found_student = next((student for student in students if student['id'] == student_id), None)
    found_course = next((course for course in courses if course['id'] == course_id), None)

    if found_student and found_course:
        marks = found_student['marks'].get(found_course['id'], 'N/A')
        print(f"Marks for student {found_student['name']} in {found_course['name']}: {marks}")
    else:
        print("Student or course not found.")



def main():
    students = []
    courses = []
    class_count = 0

    while True:
        print("\nPlease choose your choice:")
        print("1. Enter the number of students in the class")
        print("2. Enter new student")
        print("3. Number of students in the class")
        print("4. Number of courses")
        print("5. Enter new course")
        print("6. Lists Courses")
        print("7. Enter student marks")
        print("8. Find the student by ID")
        print("9. List Students")
        print("10. Show Student Marks for a Course")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 2:
            students.append(input_students_information())
            class_count = update_number_of_students(class_count, 1)
        elif choice == 1:
            class_count = input_number_of_students()
            students = [input_students_information() for _ in range(class_count)]
        elif choice == 3:
            print(f"Number of students in the class: {class_count}")
        elif choice == 4:
            num_courses = input_number_of_courses()
            courses = [input_course_information() for _ in range(num_courses)]
        elif choice == 5:
            courses.append(input_course_information())
        elif choice == 6:
            count_number_of_courses(courses)
        elif choice == 7:
            mark(students, courses)
        elif choice == 8:
            inp = input("Enter student ID: ")
            found_student = next((student for student in students if student['id'] == inp), None)
            if found_student:
                print(f"Student ID {inp} found. Name: {found_student['name']}, DoB: {found_student['dob']}")
            else:
                print("Student not found.")
        elif choice == 9:
            list_students(students)
        elif choice == 10:
            show_student_marks(students, courses)
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

    for student in students:
        for course in courses:
            print(f"\nMarks for {student['name']} in {course['name']}: {student['marks'].get(course['id'], 'N/A')}")

if __name__ == "__main__":
    main()
