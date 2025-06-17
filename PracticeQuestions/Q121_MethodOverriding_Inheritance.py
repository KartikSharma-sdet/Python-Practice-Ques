import Input_Keywords.input as input

# Practicing Classes and Inheritance
# Method Overriding

class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    def introduce(self):
        print(f"Hi, My name is {self.name} and my age is {self.age}.")

class Student(Person):

    def __init__(self,Name, Age,  studentId):
        super().__init__(Name, Age)
        self.studentId = studentId

    def introduce(self):

        print(f"My name is {self.name} and {self.age} and my id is {self.studentId}")

student = Student("Kartik", 22, 357)
student.introduce()


