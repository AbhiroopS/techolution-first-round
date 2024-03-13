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