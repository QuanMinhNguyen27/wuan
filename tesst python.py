class Student:
    def __init__(self, student_id, name, DoB):
        self.id = student_id
        self.name = name
        self.DoB = DoB
        self.marks = {}

    def display_student(self):
        return f"Student ID: {self.id}, Name: {self.name}, DoB: {self.DoB}"


class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name


class ManageStudent:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        while True:
            try:
                num_students = int(input("Enter the number of students in the class: "))
                if num_students > 0:
                    for _ in range(num_students):
                        student_id = int(input("Enter student ID: "))
                        name = input("Enter student name: ")
                        DoB = input("Enter student DoB: ")
                        student = Student(student_id, name, DoB)
                        self.students.append(student)
                    return num_students
                else:
                    print("Invalid input. Please enter a positive integer for the number of students.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of students.")

    def input_student_information(self):
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        DoB = input("Enter student DoB: ")
        student = Student(student_id, name, DoB)
        self.students.append(student)

    def input_number_of_courses(self):
        while True:
            try:
                num_courses = int(input("Enter the number of courses: "))
                if num_courses > 0:
                    for _ in range(num_courses):
                        course_id = int(input("Enter course ID: "))
                        course_name = input("Enter course name: ")
                        course = Course(course_id, course_name)
                        self.courses.append(course)
                    return num_courses
                else:
                    print("Invalid input. Please enter a positive integer for the number of courses.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the number of courses.")

    def input_course_information(self):
        course_id = int(input("Enter course ID: "))
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        self.courses.append(course)

    def input_marks(self):
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        mark = float(input("Enter marks for the student: "))

        found_student = next((student for student in self.students if student.id == student_id), None)
        found_course = next((course for course in self.courses if course.id == course_id), None)

        if found_student and found_course:
            found_student.marks[found_course.id] = mark
        else:
            print("Student or course not found.")

    def list_courses(self):
        if self.courses:
            print("List of Courses:")
            for course in self.courses:
                print(f"ID: {course.id}, Name: {course.name}")
        else:
            print("No courses have been entered yet.")

    def list_students(self):
        if self.students:
            print("List of Students:")
            for student in self.students:
                print(f"ID: {student.id}, Name: {student.name}, DoB: {student.DoB}")
        else:
            print("No students have been entered yet.")

    def show_student_marks(self):
        student_id = int(input("Enter student ID for whom you want to show marks: "))
        course_id = int(input("Enter course ID for which you want to show marks: "))

        found_student = next((student for student in self.students if student.id == student_id), None)
        found_course = next((course for course in self.courses if course.id == course_id), None)

        if found_student and found_course:
            if found_course.id in found_student.marks:
                print(
                    f"Marks for student {found_student.id} in course {found_course.id}: {found_student.marks[found_course.id]}")
            else:
                print("Marks not found for the specified student and course.")
        else:
            print("Student or course not found.")

    def main(self):
        while True:
            print("\nPlease choose your choice:")
            print("1. Enter number of students in the class and input student information")
            print("2. Enter student information")
            print("3. Enter number of courses and input course information")
            print("4. Enter course information")
            print("5. Enter marks for a student in a course")
            print("6. List courses")
            print("7. List students")
            print("8. Show student marks")
            print("9. Find student by ID")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                num_students = self.input_number_of_students()

            elif choice == 2:
                self.input_student_information()

            elif choice == 3:
                num_courses = self.input_number_of_courses()

            elif choice == 4:
                self.input_course_information()

            elif choice == 5:
                self.input_marks()

            elif choice == 6:
                self.list_courses()

            elif choice == 7:
                self.list_students()

            elif choice == 8:
                self.show_student_marks()

            elif choice == 9:
                inp = int(input("Enter student ID: "))
                found_student = next((student for student in self.students if student.id == inp), None)
                if found_student:
                    print(f"Student ID {inp} found. Name: {found_student.name}, DoB: {found_student.DoB}")
                else:
                    print("Student not found.")

            elif choice == 0:
                print("Exit!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system_manager = ManageStudent()
    system_manager.main()
