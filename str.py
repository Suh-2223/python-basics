//CONDITIONALM STATEMENTS
#QUES 1
marks=int(input("enter marks:"))
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("grade D")

#QUES 2
year=int(input("enter year"))
if year%4==0:
    print("leap year")
elif year%100!=0 and year%400==0:
    print("leap year")
else:
    print("not leap year")

#QUES 3
no=int(input("enter number:"))
if no<10:
    print("single digit")
elif no<100:
    print("double digit")
else:
    print("more than two digits")

#QUES 4
n=int(input("enter days:"))
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
else:
    print("Sunday")

#QUES 5
temp=int(input("enter temperature:"))
if temp<0:
    print("freezing")
elif 0<temp<20:
    print("cold")
elif 21<temp<35:
    print("warm")
else:
    print("hot")

#QUES 6
n=int(input("enter number:"))
if n%2==0 and n>0:
    print("postive")
elif n%2!=0 and n>0:
    print("odd")
else:
    print("negative")
 
# DATA TYPES
#QUES 1
list=[1,2,3,4,5]
print(list[0])
print(list[-1])
print(len(list))

#QUES 2
list=[1,2,3,4,5]
print(sum(list))
a=sum(list)/len(list)
print(a)

#QUES 3
lis=["Apple","Banana","Cherry"]
lis.append("Kiwi")
print(lis)
lis.insert(2,"Mango")
print(lis)

#QUES 4
list=[1,2,3,4,5]
list.remove(3)
print(list)
list.pop()
print(list)

#QUES 5
lis=[1,2,3,3,3,4,4,6]
a=lis.count(3)
b=lis.count(4)
print(a,b)

#QUES 6
numbers=[18,29,35,42,51]
no=int(input("enter the number to be search:"))
if no in numbers:
    print("number exists")
else:
    print("does not exists")

#QUES 7
li=[67,89,90,32,45]
n=int(input("enter the position:"))
b=li.index(n)
print(b)

#QUES 8
li=[67,189,90,32,45,12]
li.sort()
print("ascending:",li)
li.sort(reverse=True)
print("descending:",li)

#QUES 9
li=[67,89,90,32,45,12]
li.reverse()
print("Reverse:",li)

#SETS
#QUES 1
set={"red","green","yellow","white","black"}
print(set)

#QUES 2
set={1,2,3,3,4,5,6}
print(set)

#QUES 3
fruits={"apple","banana","kiwi","mango"}
for element in fruits:
    print(fruits)

#QUES 4
set={7,89,90,32,45,12}
set.add(90)
print(set)

#QUES 5
set={7,89,90,32,45,12}
set.remove(32)
print(set)

#QUES 6
set={7,89,90,32,45,12}
set.discard(32)
print(set)

#QUES 7
set={7,89,90,32,45,12}
set.pop()
print(set)

#QUES 8
set1={"apple","banana","kiwi","mango"}
set2={"red","green","yellow","white","black","mango"}
print(set1 | set2)
print(set1 & set2)
print(set1-set2)

#DICTIONARY
#QUES 1
dict={"India":"NewDelhi","USA":"Washington","Bangladesh":"Dhaka","Afghanistan":"Kabul","France":"Paris"}
print(dict)

#QUES 2
print(dict["India"])

#QUES 3
dict["Japan"]= "Tokyo"
print(dict)

#QUES 4
dict.update({"USA":"New York"})
print(dict)

#QUES 5
del dict["France"]
print(dict)

#QUES 6
marks={"Suman":90,"Veer":83,"Siya":56,"Athrava":67,"Rahul":98}
print(marks.keys())
#QUES 7
print(marks.values())
#QUES 8
print(marks.items())
#QUES 9
print(marks.get("Rahul"))
#QUES 10
marks.update({"Dash":56,"Farah":76,"Doe":90})
print(marks)

#QUES 11
dict={"India":"NewDelhi","USA":"Washington","Germany":"Berlin","Afghanistan":"Kabul","France":"Paris"}
dict.pop("Germany")
print(dict)

#QUES 12
dict.pop("Italy","Rome")
print(dict)

#QUES 13
dict.clear()
print(dict)

#QUES 14
student={"name":"suhani","age":20,"course":"B.tech"}
student.copy()
print(student)
student.update({"age":21})
print(student)

#QUES 16
products={"a":199,"b":67,"d":159,"c":56}
for product,price in products.items():
 if(price>100):
    print("products costing more than 100 are:",product)
 
#QUES 17
fruits={"apple":120,"banana":90,"kiwi":150}
if "apple" in fruits:
    print("apple exists:")
else:
    print("does not exists")

#FUNCTION
#QUES 1
def fun():
    print("Hello,world!")
fun()

#QUES 2
def fun(name):
    print("hello,",name)
fun("Bob")

#QUES 3
def sum(a,b):
    print("sum of two numbers:",a+b)
sum(10,9)

#QUES 4
def sq(n):
    return n**2
result=sq(5)
print(result)

#QUES 5
def number(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
number(9)

#QUES 6
def fun(a,b):
    return max(a,b)
result=fun(10,90)
print(result)

#QUES 7
def fun(a,b,c,d,e):
   return (a+b+c+d+e)/5
result=fun(1,2,3,4,5)
print(result)


#QUES 8
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
result=factorial(5)
print(result)

