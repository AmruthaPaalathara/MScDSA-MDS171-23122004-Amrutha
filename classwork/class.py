class student():  # data collection # a blue print where it store objects

#     #data members/attributes of the class
#     #name , email , phone

#     #members function=the function that a class is doing
    def __init__(self):   #initializing the property of that function
        self.name="Amrutha"       #to refer current object/to initialize the current class is operating
        self.email="amrutha@gmail.com"
        self.phone=9452736610    #self is constructor here. i.e., construct the variables
    
    def printsStudent(self):
        print("Name : {} \n Email : {} \n Phone: {} ".format(self.name,self.email,self.phone))
        
#    def __str__(self):
#         pass
detail=student()
detail.printsStudent()
print(detail.name)

class Student:                                         #int , str , float are classes
    def __init__(self,a,b):
        self.name = a
        self.stu_class = b

    def __str__(self):
        return self.name
abc=Student("Arjun","MBBS")   #here abc is an object
print(abc.name,abc.stu_class)
print(abc)

print(type(abc))


# Q.1)Create a class restaurant , that accepts item name and quantity as input
#     Inside your class you are having the item  and its price as dictionary
#     Create a function calculate cost that prints the itemname , quantity and price 

class restaurant:
    def __init__(self,item,qty):    #__init__ is a member function
        self.item=item   #variables with self aare called self variables
        self.quantity=qty
        self.menu={"rice":35 ,"veg curry": 45}
    def findCost(self):   #functions inside the class is called member function
        total=0
        total=self.quantity*self.menu[self.item]
        print(self.item,self.quantity,total)
order1=restaurant("rice",4)
order1.findCost()
order2=restaurant("veg curry",2)
order3=restaurant("rice",1)
order2.findCost()
order3.findCost()