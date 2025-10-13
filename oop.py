class displayName:
    def __init__(self ,name:str ,age:int ,lec):
        self.name=name
        self.age=age
        self.lecturer=lec
    def __repr__(self):
        return f"My name is {self.name} and im {self.age} years old"
    def getSubject(self, subject:str):
        return f"I am doing {subject} in school thought by {self.lecturer.lecName}"

class lecturers:
    def __init__(self ,lecName:str ,unit:int):
        self.lecName=lecName
        self.unit=unit

natho=lecturers("Mwangi",302)
name1=displayName("nathan" ,25 ,natho)
# print(name1.lecturer.lecName)
print(name1.getSubject("Computer Science")) 

# Example demonstrating class attributes and instance attributes

class Student:
    # Class attribute
    school_name = "Greenwood High"

    def __init__(self, name, grade):
        # Instance attributes
        self.name = name
        self.grade = grade

    def display_info(self):
        return f"Student: {self.name}, Grade: {self.grade}, School: {Student.school_name}"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def school_motto():
        return "Knowledge is Power"

# Creating instances
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Accessing instance and class attributes
print(student1.display_info())
print(student2.display_info())

# Changing class attribute using class method
Student.change_school("Sunrise Academy")

print(student1.display_info())
print(student2.display_info())

# Accessing static method
print(Student.school_motto())

# Example demonstrating inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} I teach {self.subject}."

# Creating instances
person = Person("John", 40)
teacher = Teacher("Ms. Smith", 35, "Mathematics")

print(person.introduce())
print(teacher.introduce())

# Example demonstrating inheritance of class attributes

class Animal:
    kingdom = "Animalia"  # Class attribute

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    species = "Canis lupus familiaris"  # Additional class attribute

# Accessing inherited class attribute
print(Dog.kingdom)  # Output: Animalia
print(Dog.species)  # Output: Canis lupus familiaris

# Instance also has access to class attributes
dog1 = Dog("Buddy")
print(dog1.kingdom)  # Output: Animalia
print(dog1.species)  # Output: Canis lupus familiaris

# Define a class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # list of grades

    def average(self):
        # Use a for loop to calculate the average grade
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)


# Create multiple Student objects
students = [
    Student("Alice", [80, 90, 85]),
    Student("Bob", [70, 75, 80]),
    Student("Charlie", [95, 100, 98])
]
# print([student.name for student in students])
# Use a for loop to go through all students
for student in students:
    print(f"{student.name}'s average grade: {student.average():.2f}")
