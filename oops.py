#OOPS
#QUES 1
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("details of students:",(self.name),(self.age))

s1=Student("Alice",20)
s2=Student("Gemmi",25)

s1.details()
s2.details()

#QUES 2
class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def show_details(self):
        print("details of car are:",(self.brand),(self.price))

Car1=Car("Tesla",50000)
Car2=Car("BMW",70000)

Car1.show_details()
Car2.show_details()

#QUES 3
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def detail(self):
        print("details of employee are:",(self.name),(self.salary))

emp1=Employee("Rahul",70000)
emp2=Employee("Rohit",90000)

emp1.detail()
emp2.detail()

#QUES 4
class Mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def information(self):
        print("details of mobile are:",(self.brand), ",",(self.model))

model1=Mobile("apple","promax")
model2=Mobile("oneplus","nodelite")
model3=Mobile("motorola","ce3")

model1.information()
model2.information()
model3.information()

#QUES 5
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("descriptions of book are:",(self.title), ",",(self.author))

b1=Book("Harry Porter","J.K.Rowling")
b1.display()

#QUES 6
class College:
 college_name="BBD"

 def __init__(self,name):
        self.name=name
        
 def information(self):
        print("details of student are:",(self.name))

s1=College("Suman Saini")

print("collegename is:",College.college_name)
s1.information()

#QUES 7
class Bike:
    def __init__(self,brand,color):
        self.color=color
        self.brand=brand
    def start(self):
        print(self.color,self.brand,"bike is starting")

b1=Bike("Apache","white")
b2=Bike("Bullet","black")
b1.start()
b2.start()

#QUES 8
class Laptop:
    def __init__(self,brand,RAM):
        self.RAM=RAM
        self.brand=brand
    def start(self):
        print("details of laptop are:",self.brand,self.RAM)

l1=Laptop("HP","6GB")
l2=Laptop("ASUS","5GB")
l1.start()
l2.start()


