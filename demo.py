name=input("enter your name:")
int("hello,world",name)
age=int(input("enter your age:"))
print("Age is:",age)

#ARITHEMATIC OPERATORS
#QUES-1
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
sum=a+b
diff=a-b
pro=a*b
quo=a/b
print("the sum is:",sum)
print("the difference is:",diff)
print("the product is:",pro)
print("the quotient is:",quo)

#QUES-2
a=15
b=4
print("the floor division is:",(a//b))
print("the remainder is:",(a%b))
print("the power is:",(a**b))

#QUES-3
n=40
p=15
tc=(3*p)+(2*n)
print("total cost is:",tc)

#QUES-4
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))
d=float(input("enter value of d:"))
e=float(input("enter value of e:"))
f=float(input("enter value of f:"))
print("the average is:",(a+b+c+d+e)/5)

#QUES-5
n=int(input("enter value of n:"))
print("square is:",(n**2))
print("cube is:",(n**3))
print("square root is:",(n**0.5))

#QUES-6
ts=int(input("enter value of ts:"))
minutes=ts//60
seconds=ts%60
print(minutes)
print(seconds)

#QUES-7
distance=120
time=3
print("average speed is:",(distance/time))

#QUES-8
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
if a%b==0:
 print(a, "is multiple of",b)
else:
 print(a ,"is not multiple of", b)

#QUES-9
p=int(input("enter value of p:"))
r=int(input("enter value of r:"))
t=int(input("enter value of t:"))
print("the simple interest is:",(p*r*t)/100)

#QUES-10
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
print("the rounded quotient is:",(a//b))


#COMPARISON OPERATORS
#QUES-1
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
if a==b:
 print(a,"is equal to",b)
else:
 print(a,"is not equal to",b)

#QUES-2
if a>b:
 print(a,"is greater than",b)
else:
 print(a,"is less than",b)

#QUES-3
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
if a<b and a<c:
    print(a,"is smallest")
elif b<a and b<c:
    print(b,"is smallest")
else :
    print(c,"is smallest")
    
#QUES-4
marks=float(input("enter marks:"))
if marks>=40:
    print("pass")
else:
    print("fail")

# QUES-5
age=int(input("enter age:"))
if age>=18:
    print("eligibe to vote")
else:
    print("not eligible to vote")

# QUES-6
n=int(input("enter number:"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")

# QUES-7
a=input("enter a string:")
b=input("enter a string:")
if a==b:
    print("same string")
else:
    print("different string")

# QUES-8
A=int(input("enter salary of first employee:"))
B=int(input("enter a salary of second employee:"))
if A>B:
    print("employee a earns more")
else:
    print("employee b earns more or equal")

# QUES-9
n=int(input("enter a number:"))
if n>10 and n<50:
    print("lies between")
else:
  print("not lies between")

# QUES-10
year=int(input("enter year:"))
if year%4==0:
    print("leap year")
elif year%100!=0 and year%400==0:
    print("leap year")
else:
    print("not leap year")

#LOGICAL OPERATOR
# QUES-1
Maths=int(input("enter marks in maths:"))
Science=int(input("enter marks in science:"))
if Maths>=40 and Science>=40:
    print("Pass")
else:
    print("fail")

# QUES-2
n=int(input("enter amount:"))
membership=input("check for membership:")
if n>1000 and membership=="yes":
    print("gets a discount")
else:
    print("not discount")

# QUES-3
n=int(input("enter number:"))
if n%3 !=0:
    print("not divisble by 3")
else:
    print("divisible by 3")

# QUES-4
age=int(input("enter age:"))
if age>13 and age<19:
    print("teenager")
else:
    print("not teenager")

# QUES 5
Age=int(input("enter age:"))
if Age>=18:
    print("eligible to vote")
else:
    print("not eligibe to  vote")
if Age>=18 and Age<=70:
    print("eligible to vote and drive")
else:
    print("not eligibe to  vote and drive")

#QUES 6
attend=int(input("enter attendance:"))
assign=input("assignment submitted? ")
if attend>=75 and assign=="yes":
 print("sit for exams")
else:
 print("do not sit for exam")

#QUES 7
year=int(input("enter year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")

#QUES 8
day=input("enter day:")
holiday=input("enter holiday:")
if day=="Sunday" or holiday =="yes":
    print("relax")
else:
    print("not relax")

#QUES 9
no=int(input("enter a number:"))
if no%3==0 and no%5==0:
    print("no is divisible by both 3 and 5")
else:
    print("not divisible")

# QUES 10
username=input("enter username:")
password=input("enter password:")
if username=="admin" and password =="1234":
    print("login successful")
else:
    print("login failed")

# ASSIGNMENT OPERATORS
# QUES 1
a=10
print(a)

# QUES 2
a=int(input("enter a number:"))
a+=5
print(a)

# QUES 3
a=int(input("enter a number:"))
a-=3
print(a)

# QUES 4
a=int(input("enter a number:"))
a*=2
print(a)

# QUES 5
a=int(input("enter a number:"))
a/=2
print(a)

# QUES 6
a=int(input("enter a number:"))
a//=3
print(a)

# QUES 7
n=int(input("enter a number:"))
n%=7
print(n)

# QUES 8
n=int(input("enter a number:"))
n**=3
print(n)



