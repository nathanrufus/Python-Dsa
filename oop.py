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