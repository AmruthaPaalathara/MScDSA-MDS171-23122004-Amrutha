class student:
    def __init__(self,name,phone): #to initialize the data members
        self.name=name
        self.phone=phone
    def printStudent(self):
        print(self.name,self.phone)