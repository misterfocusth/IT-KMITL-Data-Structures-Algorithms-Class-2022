class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGpa(self):
        return self.gpa

    def printDetail(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("GPA:", self.gpa)
