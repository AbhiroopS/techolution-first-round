# Problem 1: Student and Course Management
# Question:
# Implement a simple student and course management system using OOP. Create classes ‘Student’ and ‘Course’. The ‘Student’ class should have attributes for student details (name, ID, etc.) and a method to calculate the GPA. The ‘Course’ class should have a list of enrolled students and methods to add a student, remove a student, and calculate the average GPA of all students in the course.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id =student_id
        self.courses = {}
    
    def enroll(self, course):
        self.courses[course.course_id] = course
        course.add_student(self)
    
    def calculate_gpa(self):
        total_grade_points= 0
        total_credits = 0
        for course_id, course in self.courses.items():
            total_grade_points += course.grade_points * course.credits
            total_credits += course.credits
        if total_credits == 0:
            return 0
        else:
            return total_grade_points/total_credits

    def display_courses(self):
        print(f"Courses enrolled by {self.name}: ")
        for course_id, course in self.courses.items():
            print(f"{course.title} (ID:{course_id})")

class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.students = {}
        self.credits = credits
        self.grade_points = grade_points
    
    def add_student(self, student):
        self.students[student.student_id] = student
    
    def remove_student(self, student):
        if student_id in self.students:
            del self.students[student_id]

    def display_students(self):
        print(f"Studnets enrolled in {self.title}: ")
        for student_id, student in self.students.items():
            print(f"{student.name} (ID:{student_id})")


