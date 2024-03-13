# Problem 1: Student and Course Management
# Question:
# Implement a simple student and course management system using OOP. Create classes ‘Student’ and ‘Course’. The ‘Student’ class should have attributes for student details (name, ID, etc.) and a method to calculate the GPA. The ‘Course’ class should have a list of enrolled students and methods to add a student, remove a student, and calculate the average GPA of all students in the course.

from Student import Student
from Course import Course

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