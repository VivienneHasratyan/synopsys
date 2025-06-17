class Tutor:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

class Course:
    def __init__(self, title, duration, level):
        self.title = title
        self.duration = duration
        self.level = level
        self.tutor = None

    def assign_tutor(self, tutor):
        self.tutor = tutor
        print(f"Tutor {tutor.name} assigned to course '{self.title}'.")

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.profile = ""
        self.tutor = None

    def register(self):
        print(f"Student {self.name} registered with email {self.email}.")

    def update_profile(self, info):
        self.profile = info
        print(f"{self.name}'s profile updated: {self.profile}")

    def enroll(self, course):
        self.tutor = course.tutor
        print(f"{self.name} enrolled in course '{course.title}' (Level: {course.level}, Duration: {course.duration}h).")
        if self.tutor:
            print(f"Tutor for the course: {self.tutor.name} ({self.tutor.expertise})")

class CoursePlatformFacade:
    def register_student(self, name, email):
        student = Student(name, email)
        student.register()
        return student

    def enroll_student_in_course(self, student, course):
        student.enroll(course)

if __name__ == "__main__":
    # Facade
    platform = CoursePlatformFacade()

    # Create tutor and course
    tutor = Tutor("Dr. Aram", "Data Science")
    course = Course("Intro to AI", 40, "Beginner")
    course.assign_tutor(tutor)

    # Register and enroll student
    student = platform.register_student("Lilit", "lilit@example.com")
    student.update_profile("Computer Science major, interested in AI.")
    platform.enroll_student_in_course(student, course)