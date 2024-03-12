# Problem 1: Student and Course Management
# Question:
# Implement a simple student and course management system using OOP. Create classes ‘Student’ and ‘Course’. The ‘Student’ class should have attributes for student details (name, ID, etc.) and a method to calculate the GPA. The ‘Course’ class should have a list of enrolled students and methods to add a student, remove a student, and calculate the average GPA of all students in the course.


class Student:  # Definition of Student Class, contains attributes 'name', 'student_id' and methods like 'calculate_gpa()', 'enroll()' and 'display_courses()'
    def __init__(self, name, student_id):
        self.name = name
        self.student_id =student_id
        self.courses = {}
    
    def enroll(self, course): # Function to add Student to a Course
        self.courses[course.course_id] = course
        course.add_student(self)
    
    def calculate_gpa(self): # Function to calculate total GPA of Student in Course. returns GPA Value
        total_grade_points= 0
        total_credits = 0
        for course_id, course in self.courses.items():
            total_grade_points += course.grade_points * course.credits
            total_credits += course.credits
        if total_credits == 0:
            return 0
        else:
            return total_grade_points/total_credits

    def display_courses(self): # Function to print Courses that student is enrolled in
        print(f"\nCourses enrolled by {self.name}: ")
        for course_id, course in self.courses.items():
            print(f"{course.title} (ID:{course_id})")

class Course: # Definition of Course Class, contains attributes 'title', 'course_id', 'students', etc. and methods like 'add_student()', 'remove_student()' and 'calculate_average_gpa()', etc.
    def __init__(self, title, course_id, credits, grade_points):
        self.title = title
        self.course_id = course_id
        self.students = {}
        self.credits = credits
        self.grade_points = grade_points
    
    def add_student(self, student): # Function used by Student Class to enroll Students to a Course
        self.students[student.student_id] = student
    
    def remove_student(self, student): # Removes Student from Course, needs Student ID as argument
        if student in self.students:
            del self.students[student]

    def display_students(self): # Displays Students enrolled in Course
        print(f"\nStudents enrolled in {self.title}: ")
        for student_id, student in self.students.items():
            print(f"{student.name} (ID:{student_id})")

    def calculate_average_gpa(self): # Prints out average GPA of all students enrolled in the Course
        total_gpa = 0
        num_students = len(self.students)
        if num_students == 0:
            return 0
        for student in self.students.values():
            total_gpa += student.calculate_gpa()
        return "{:.2f}".format(total_gpa / num_students)

# Creating Student class Objects with Student Name and ID
student1 = Student("Alice", 1) 
student2 = Student("Bob", 2)

# Creating Course class Objects with Course Name, ID, Credits, and Grade Points
course1 = Course("Python Programming", 101, 3, 4) 
course2 = Course("Data Structures", 102, 4, 3)

# Enrolling Students into Courses
student1.enroll(course1)
student2.enroll(course1)
student2.enroll(course2)

# Displaying which Course each student is in
student1.display_courses()
student2.display_courses()

 # Displaying Students in each course along with average GPA of all students enrolled in that Course
course1.display_students()
print(f"Average GPA of all students: {course1.calculate_average_gpa()}")
course2.display_students()
print(f"Average GPA of all students: {course2.calculate_average_gpa()}")