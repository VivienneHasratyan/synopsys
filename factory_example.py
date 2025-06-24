import abc

class iPerson(abc.ABC):
    @abc.abstractmethod
    def person_do_stuff(self):
        """Each person must element this"""

class Student(iPerson):
    def __init__(self):
        self.name = "Student name"
        self.age = "Student age"

    def person_do_stuff(self):
        print("I am a Student")

class Lecturer(iPerson):
    def __init__(self):
        self.name = "Lecturer name"
        self.age = "Lecturer age"

    def person_do_stuff(self):
        print("I am a Lecturer")

class iPersonCreator(abc.ABC):
    @abc.abstractmethod
    def create_person(self):
        """Factory method"""

class StudentCreator(iPersonCreator):
    def create_person(self):
        return Student()

class LecturerCreator(iPersonCreator):
    def create_person(self):
        return Lecturer()


if __name__ == "__main__":
    person_type = input("Choose Student/Lecturer: ")
    if person_type == "Student":
        factory = StudentCreator()
    elif person_type == "Lecturer":
        factory = LecturerCreator()
    else:
        print("Invalid input")

person = factory.create_person()
person.person_do_stuff()