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


#INHERITANCE
class Animal:
  def speak(self):
   print("animals make sound")

class Dog(Animal):
  def bark(self):
   print("dog barks")

d=Dog()
d.speak()
d.bark()

#ENCAPSULATION
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
     self.__balance += amount
    def get_balance(self):
        return self.__balance

acc=BankAccount("Alice",10000)
acc.deposit(5000)
print(acc.get_balance())

#QUES 1
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
            print("name:",self.name)
            print("roll_no:", self.roll_no)
            print("marks:",self.marks)

s1=Student("Alie",32,67)
s1.display()

#QUES 2
class Circle:
    def __init__(self,radius):
        self.radius=radius 

    def area(self):
        print("area of circle:",3.14*(self.radius**2))

    def perimeter(self):
        print("perimeter of circle:",2*3.14*self.radius)

r1=Circle(7)
r1.area()
r1.perimeter()

#QUES 3
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)

e_1=Employee("Sam",32,67000)
e_1.display()

#QUES 4(SINGLE INHERITANCE)
class Vehicle:
    def start(self):
        print("vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("car starts")

c1=Car()
c1.start()
c1.drive()

#QUES 5(MULTILEVEL INHERITANCE)
class Grandfather:
    def show(self):
        print("grandfather")

class Father(Grandfather):
    def show(self):
        print("father")

class Son(Father):
    def show(self):
        print("son")

s1=Son()
s1.show()
s1.show()
s1.show()

#QUES 6(MULTIPLE INHERITANCE)
class Teacher:
    def show(self):
        print("Teacher")

class Student:
    def show(self):
        print("Student")

class TeachingAssistant(Teacher,Student):
    def show(self):
        print("TeachingAssistant")
    
ta=TeachingAssistant()
ta.show()

#QUES 7(Polymorphism)
class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("barks")

class Cat(Animal):
    def sound(self):
        print("Meow")
    
an=Animal()
d=Dog()
c=Cat()
c.sound()
d.sound()

FILE HANDLING
#QUES 1
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r") as file:
 content=file.read()
 print(content)

#QUES 2
 content=file.readline()
 print(content)

#QUES 3
 content=file.readlines()
 print(content)

QUES 4
 for f1 in file:
  print(f1)

#QUES 5
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r") as file:
    count=0
    for line in file:
        count+=1
    print("number of lines:",count)

#QUES 6
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","w") as file:
 file.write("Suman,21,Assam\n")
 file.write("Srijal,20,UP\n")
 file.write("Riya,19,MP\n")
print("data written successfully")

#QUES 7
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r") as file:
    content=file.read()
    print(content)

#QUES 8
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","a") as file:
    file.write("Karan,23,Pune\n")

#QUES 9
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r") as file:
     a=file.read()
     print(a)

#QUES 10
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r+") as file:
    a=file.read()
    a=a.replace("Amit","Amit Kumar")
    file.seek(0)
    file.write(a)
    
#QUES 11
with open("c:/Users/suhani singh/OneDrive/Desktop/students.txt","r+") as file:
    file.seek(0,2)
    file.write("\nSneha,20,Hyderabad")

MODULES
import math

# QUES 1
print("square root is:",math.sqrt(625))

#QUES 2
print("factorial is:",math.factorial(6))

#QUES 3
print("floor value:",math.floor(4.7))
print("ceiling value:",math.ceil(4.7))

#QUES 4
print("power will be:",math.pow(5,3))

#QUES 5
print("absolute value:",math.fabs(-18))

#QUES 6
a=(math.radians(90))
print("sin value:",(math.sin(a)))
print("cos value:",(math.cos(a)))
print("tan value:",(math.tan(a)))

#QUES 7
print("GCD of:",math.gcd(36,60))

#QUES 8
print("value of:",math.exp(3))

# QUES 9
print("logarithmic base:",math.log(1000,10))

#QUES 10
print("convert into radian:",math.radians(180))

RANDOM
import random
#QUES 1
print("a random no bte 1 and 10;",random.randint(1,10))

#QUES 2
print("a random  floating no bte 0 and 1;",random.uniform(0,1))

#QUES 3
list=[10,20,30,40,50]
print(random.choice(list))

#QUES 4
list=[1,2,3,4,5]
print(random.shuffle(list))
print(list)

#QUES 5
print(random.randrange(2,20,2))

#QUES 6
integers=random.sample(range(10,100),5)
print(integers)

#QUES 7
print("roll a dice:",random.randint(1,6))

#QUES 8
import string
pswd= " "
for i in range(9):
    pswd +=random.choice(string.ascii_letters)

print("generated password:",pswd)

#QUES 9
import string
pswd= " "
characters=string.ascii_letters+ string.digits+ string.punctuation
for i in range(9):
    pswd +=random.choice(characters)

print("generated password:",pswd)

#QUES 10
integers=random.sample(range(1,20),4)
print(integers)

#DATETIME
import datetime
#QUES 1
print(datetime.datetime.now())

#QUES 2
print(datetime.date.today())

#QUES 3
a=(datetime.date.today())
print(a.year)
print(a.month)
print(a.day)

#QUES 4
dt=datetime.datetime.now()
formatted=dt.strftime("%A,%B %d,%Y %I:%M:%S %p")
print("formatted date and time:",formatted)

#QUES 5 
dob=input("enter date of birth(YYYY-MM-DD):")
db=datetime.date.fromisoformat(dob)
td=datetime.date.today()
age=td.year - db.year 
print("age is:",age)

#QUES 7
a=datetime.date.today()
futuredate=a + datetime.timedelta(days=10)
print("date after 10 days:",futuredate)

#QUES 8
d1=datetime.date(2023,12,25)
d2=datetime.date(2025,11,30)
diff=abs(d1-d2)
print("difference in days:",diff.days)

#QUES 9
dob=input("enter date of birth(YYYY-MM-DD):")
dob=datetime.date.fromisoformat(dob)
today=datetime.date.today()
if dob.month==today.month and dob.day==today.day:
    print("happy birthday!")
else:
    print("today is not your birthday.")

        


