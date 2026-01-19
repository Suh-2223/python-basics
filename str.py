#CONDITIONAL STATEMENTS
#QUES 1
n=int(input("enter number:"))
if  n>0:
    print("postive")
elif n<0:
    print("negative")
else:
    print("zero")

 #QUES 2
Age=int(input("enter age:"))
if Age>=18:
    print("eligible to vote")
else:
    print("not eligibe to  vote")

 #QUES 3
n=int(input("enter number:"))
if  n%2==0:
    print("even")
else:
    print("odd")

#QUES 4
a=int(input("enter number:"))
b=int(input("enter number:"))
if  a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)

#QUES 5
n=int(input("enter number:"))
if  n%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

#QUES 6
marks=int(input("enter marks:"))
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("grade D")

#QUES 7
year=int(input("enter year"))
if year%4==0:
    print("leap year")
elif year%100!=0 and year%400==0:
    print("leap year")
else:
    print("not leap year")

# QUES 8
no=int(input("enter number:"))
if no<10:
    print("single digit")
elif no<100:
    print("double digit")
else:
    print("more than two digits")

# QUES 9
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

# QUES 10
temp=int(input("enter temperature:"))
if temp<0:
    print("freezing")
elif 0<temp<20:
    print("cold")
elif 21<temp<35:
    print("warm")
else:
    print("hot")

# QUES 11
n=int(input("enter number:"))
if n%2==0 and n>0:
    print("postive and even")
elif n%2!=0 and n>0:
    print("positive and odd")
else:
    print("negative")

# QUES 12
pswd=input("enter password:")
if pswd== "admin123":
     print("access granted")
else:
     print("access denied")

# QUES 13
a=int(input("enter first side of triangle:"))
b=int(input("enter second side of triangle:"))
c=int(input("enter third side of triangle:"))
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("not a valid triangle")

# QUES 14
m=int(input("enter marks in math:"))
s=int(input("enter marks in science:"))
e=int(input("enter marks in english:"))
total=m+s+e
if total>=35:
    print("pass")
else:
    print("fail")

# QUES 15
ch=input("enter a character:")
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")
    
# DATA STRUCTURE
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
print(set1.union(set2))
#QUES 9
print(set1 & set2)
#QUES 10
print(set1-set2)

#QUES 11
set1={"apple","banana","kiwi","mango"}
a=set1.copy()
a.add("strawberry")
a.remove("banana")
print(set1)
print(a)

#QUES 12
a.clear()
print(a)

#QUES 13
list1=[1,2,3,3,9,4,5,6,9]
set1=set(list1)
print(set1)

#QUES 14
a=input("enter a string:")
unique_chars=set(a)
print("unique characters are:",unique_chars)

#QUES 15
listf=["arun","bob","charlie","david","sam"]
listc=["charlie","david","eva","frank","simran"]
setf=set(listf)
setc=set(listc)
print("students who play football:",setf)
print("students who play cricket:",setc)
print("students who play both sports are:",setf&setc)

QUES 16
# print("students who played only cricket are:",setf-setc)

#QUES 17
sentence=input("enter a sentence:")
a=sentence.split()
unique_words=set(a)
print("unique words are:",unique_words)

#QUES 18
set1={"apple","banana","kiwi","mango"}
set2={"banana","kiwi","mango","apple"}
a=set1==set2
print(a)

#QUES 19
set1={"pink","blue","white"}
set2={"white","red","purple"}
if set1&set2:
    print("common elements exist")
else:
    print("no common elements")

#QUES 20
list1=[1,2,3,3,9,4,5,6,9]
set1=set(list1)
unique_elem=list(set1)
print("list of unique elements:",unique_elem)

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

#QUES 15
sentence=input("enter a sentence:")
a=sentence.split()
freq={}
for word in a:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("word frequency:",freq)

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

#QUES 18
marks={
    "Suman":90,
    "Veer":83,
    "Siya":56,
    "Athrava":67,
    "Rahul":98}
topper=max(marks,key=marks.get)
print("topper is:",topper)
print("highest marks:",marks[topper])

#QUES 19
list1=["name","age","city"]
list2=["Amit",25,"Delhi"]
dict1=dict(zip(list1,list2))
print(dict1)

#QUES 20
dict={"name":"suhani","age":20,"course":"B.tech"}
swapped_dict={value:key for key,value in dict.items()}
print(swapped_dict)

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
def fun(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count

result=fun("Hello World")
print("number of vowels:",result)

#QUES 9
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
result=factorial(5)
print(result)

#QUES 10
def palindrome(s):
    s=s.lower()
    s=s[::-1] #reverse a string and compare
    return s

text=input("enter a string:")
if palindrome(text):
    print("palindrome")
else:
    print("not palindrome")


