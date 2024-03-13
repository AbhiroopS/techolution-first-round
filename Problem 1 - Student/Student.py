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