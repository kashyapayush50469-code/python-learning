'''# print("Hello, world!") 
# print("Welcome to practicing python.")
# print("This is a simple python script.")
# name = "ayush"
# friend = "john"
# anotherfriend = "doe"
# print("Hello" + friend + " and " + anotherfriend + " my name is " + name)
# niraj = He said ,
# Hi ayush 
# Hey I am good
# "i wanted to eat an apple"'''
'''# apple = "he said ", "I want to eat food"
# print(niraj)
# print(type(niraj))
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print("lets use a for loop\n")
# for character in apple:
#     print(character)
# print("lets use a while loop\n")
# i =0
# while i < len(name):
#     print(name[i])
#     i += 1
# print("lets useslicing\n")
# print(name[0:3])
# print(name[1:4])
# print(name[:4])
# print(name[2:])
# print(name[-4:-1])
# print(name[-4:])

# print("lets use some string methods\n")
# a = "ayush"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.replace("ayush", "niraj"))
# print(a.find("y"))
# print(a.index("u"))
# print(a.count("a"))
# print(a.isalnum())
# print(a.isalpha())
# str1 = "HELLO WORLD"
# print(str1.isupper())
# str1 = "hello world"
# print(str1.islower())
# str1 = "welcome to my house"
# print(str1.endswith("to"))
# print(str1.startswith("welcome"))
# print(len(str1))
# print(str1.split(" o ")) #split by space
# print(str1.split(" w "))
# str1 = "How are you"
# print(str1.isprintable())
# str1 = "       "
# print(str1.isspace())
# str1 = "world trade organization" 
# print(str1.istitle())
# str1 = "world health organization"
# print(str1.title())
# str1 = "sarry!!!!!!!!!!!"
# print(str1.rstrip("!"))
# str1 = "Hello world"
# print(str1.format())
# print(str1.center(30))
# print(str1.encode())
# print(str1.expandtabs())
# print(str1.swapcase())
# print(str1.partition("world"))
# print(str1.zfill(30))
# print(str1.lstrip("H"))
# print(str1.rjust(20))
# print(str1.maketrans("H", "A"))
# print(str1.translate(str1.maketrans("H", "A")))
# print(str1.removeprefix("Hello"))
# print(str1.removesuffix("world"))
# print(str1.casefold())
# print(str1.replace("world", "universe"))
# print(str1.center(50, "#"))
# print(str1.format_map({"Hello": "Hi", "world": "everyone"}))
# print(str1.splitlines())
# print(str1.isascii())

appleprices = 210
budget = 200
if(appleprices < budget):
    print("I will buy apple")
else:
    print("I will not buy apple")

applesprices =180 
if(applesprices < budget):
    print("I will buy an apple")
elif(applesprices == budget):
    print("I will buy an apple with  my entire budget")
else:
    print("I will not buy an apple")

a = 18
if(a > 18):
    print("you are eligible for voting")
elif(a == 18):
    print("you are just eligible for voting")
else:
    print("you are not eligible for voting")

num = 8
if(num % 2 == 0):
    print("the number is even number") 
else:
    print("the number is odd number")

num = 15 
if(num % 2 == 0):
    print("the number is even number")
else:
    print("the number is odd number")

num = 15 
if(num <0):
    print("The number is negative")
elif(num>0):
    if(num<=10):
        print("The number is between 1 - 10")
    elif(num> 10 and num<=20):
        print("The number is between 11 -20")
    else:
        print("The number is greter than 20")
else:
    print("The numbe is zero")

age = 25 
if(age <18):
    print("you are a minor")
elif(age >=18 and age <60):
    print("you are an adult")
else:
    print("you are a senior citizen")

marks = 85 
if(marks >=90):
    print("you got A grade")
elif(marks >= 75 and marks <90):
    print("you got b grade")
elif(marks >= 60 and marks <75):
    print("you got c grade")
elif(marks >= 40 and marks <60):
    print("you got d grade")
else:
    print("you got f grade") 

marks = 40
if (marks >= 100):
    print("you got A grade")
elif (marks>=75 and marks <90):
    print("you got B grade")
elif(marks >= 60 and marks < 75):
    print("you got c grade")
elif(marks >= 35 and marks < 60):
    print("you got d grade")
else:
    print("you got f grade")

name  = "ayush"
for i in name:
    print(i)
i = 0
while i < 5:
    print(i)
    i += 1 
print("done")
for b in range(2, 10 , 2):
    print(b)  

count = 5 
while(count > 0):
    print(count)
    count = count -1
else:
    print("I am inside else")
# for i in range(12):
#     if(i % 2 ==0):
#         print (i)
#     else:
#         print("even number")  

# for i in range(12):
#     print("16*",i+1, "=", 16*(i+1))
#     if(i == 10):
#         break
# print("loop ko break kar diya")
# for i in range(10):
#     if(i % 2 ==0):
#         continue
#     print(i)
# i = 0
# while True:
#     print(i)
#     i = i+1
#     if(i%100 ==0):
#         break 

# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isgreater(a, b):

#     if(a > b):
#         print("first number is greater")
#     else:
#         print("second number is greater")
# def islesser(a, b):
#     pass 

# a = 9 
# b = 8
# isgreater(a, b)
# calculateGmean(a, b) 

# def average (a = 5, b = 6):
#     print("The average is", (a + b)/2) 
# average(4, 6)
# average(b = 9, a = 21)
# def average(a, b, c =1):
#     print("The average is", (a + b + c)/3) 

# average(5, 6)
# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + 1
#         print("The average is:", sum/len(numbers))
#         return sum/len(numbers) 
# def name(**name):
#     print(type(name))
#     print("Hello", name["fname"], name["mname"], name["lname"]) 
#     name(fname = "tom", mname = "john", lname = "harry") 
# print(name) 

# marks = [3, 4, 5, 6, 8, "aysuh", True, 23, 45, 674, 897, 908]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])
# if  7 in marks:
#     print("yes 7 is present in marks")
# else:
#     print("7 is not present in marks")
# if "ush" in "ayush":
#     print("yes")
# else:
#     print("no") 

# print(marks[1:5])
# print(marks[1:5:3])


# lst = [i*i for i in range(10)]
# print(lst)
# l = [1, 2, 3, 4, 5, 2, 2, 3 ,4, 5]
# print(l.append(6))
# print(l)
# print(l.count(2))
# print(l)
# print(l.index(4))
# print(l)
# print(l.reverse())
# print(l)
# l.sort()
# print(l)
# l.pop()
# print(l)
# l.remove(2)
# print(l)
# l.insert(2, 10)
# print(l)
# l.extend([20, 30, 40])
# print(l)
# l.copy()
# print(l)
# l.clear()
# print(l)

# tup = (1, 5, 6, 56, "yellow")
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# if 5 in tup:
#     print("yes 5 is present in tuple")
# else:
#     print("5 is not present i tuple")
# tuple = (1, 2, 3, 4, 5, 3, 4, 2, 2, 6, 7, 8, 9)
# a = tuple.count(3)
# print(a)
# a = tuple.index(3, 4, 8)
# print(a)
# a = len(tuple)
# print(a)
# # f string
# letter = "hey my name is {0} and i am form {1}"
# name = "ayush" 
# country  = "india" 
# print(letter.format(name, "india"))
# print(f"hey my name is {name} and i am from {country}") 
# prices = 49.09999
# print(f"The price is {prices:.2f}dollars")
# print(f"{2*40}") 

# def square(n):
#     ""Takes is a nmber n and return the square of n""
#     print(n**2) 
# square(5) 
# print(square.__doc__) 

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
# set methods
# s = {1, 2, 2, 3, 4, 4, 5}
# print(s)
# s = {"ayush", "niraj", 5, 6, 7, 7, 6}
# print(s)
# s.add(8)
# print(s)
# s.update([9, 10, 11])
# print(s)
# s.remove(5)
# print(s)
# for value in s:
#     print(value) 
# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.symmetric_difference(s2))
# print(s1.copy())
# print(s1.isdisjoint(s2))
# t1 = s1.pop()
# print(t1)
# print(s1) 

#dictinory  methods
# dic = {
#     "ayush": "student",
#     "spoon": "kitchen item",
#     }
# print(dic["ayush"])
# print(dic["spoon"])
# info = {"name": 'aysuh', "age": 15, "eligible": "true"}
# print(info)
# print(info["name"])
# print(info.get("name"))
# print(info.keys())
# print(info.values()) 
# print(info.values())

# for key in info.keys():
#     print(info[key])

# for key in info.keys():
#     print(f"The value corresponding to the key{key} is {info[key]}") 

# print(info.items())
# for key, value in info.items():
#     print(f"The value corresponding to the key{key} is {value}")
# ep1 = {122:45, 123:89, 567:69, 670:69}
# ep2 = {122:67, 566:90}
# # ep1.update(ep2) 
# # ep1.clear()
# # # ep1.popitem()
# # ep1.pop()
# # print(ep1) 
# for i in []:
#     print()
# else:
#     print("sorry no i")
# for i in range(6):
#     print(i)
#     if i == 4:
#         break 

# else:
#     print("sorry no i")

# i = 0
# while i<7:
#     print(i)
#     i = i+1 
#     if i == 5:
#         break 
# else:
#     print("sorry no i")

# for x in range(5):
#     print("interation on {} in for loop".format(x+1))
# else:
#     print("else block in loop")
# print("out of loop")

# a = 4 
# print("Multiplication table of {a} is:") 
# try:
#       for i in range(1, 11):
#           print(f"{int(a)}x{i} =  {int(a)*i}")
# except Exception as e:
#   print("sorry some error occured") 
     

#   print("some lmp lines of code ")
#   print("end of program") 
 
# try:
#     num = 1
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("number entered is not integer.")
# except IndexError:
#     print("index error")

# def func1():
#     try:
#         l = [1, 5, 6, 7]
#         l = 1
#         print(l[i]) 
#         return 1 
#     except:
#         print("some error occured")
#         return 0
#     finally:
#         print("I am always excuted") 
# x = func1()
# print(x) 

# a = 33 
# b = 3303
# print("a") if a<b else print("=") if a==b else print ("b") 
# c = 9 if a<b else 0
# print(c)
# marks = {12, 56, 32, 12, 98, 45, 1, 4}
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("jarry, awesome!")
#     index +=1 
# for index , mark in enumerate(marks, start = 3):
#     print(mark)
#     if(index == 3):
#         print("jarry, awesome") 

#import type programe 
# import math 
# math.floor(4.2343)

# result = math.sqrt(9) 
# print(result)
# from math import sqrt, pi

# result = math.sqrt(9)* pi 
# print(result) 
# import math as m
# result = m.sqrt(9)*m.pi
# print(result) 
# import math 
# print(dir(math))
# print(math.nan, type(math.nan))

# import math as math_builtin_python
# result = math_builtin_python.sqrt(9)* math_builtin_python.pi
# print(result) 



# from main import welcome, main
# from main import*
# import math 

# # print(dir(math))
# print(math.nan, type(math.nan))
# welcome()
# print(main)

# import os 
# if(not os.path.exists("jyoti")):
#     os.mkdir("jyoti") 
    
# for i in range(0, 20):
#     os.mkdir(f"jyoti/day{i+1}")   
#     #  os.rename(f"jyoti/day{i+1}", f"jyoti/nandinee{i+1}")

# import os 
# folders = os.listdir("jyoti")

# print(folders)
# print(os.getcwd) 
# os.chdir("/users")
# print(os.getcwd()) 
#local and global veribleas 
# x = 4 
# print(x) 

# def hello():
#     x = 5 

#     print(f"The local x is {x}") 
#     print("Hello ayush") 

# print(f"The global x is {x}") 

# x = 10  

# def my_function():
#     global x 
#     x = 4
#     y = 5 
#     print(y)

# my_function()
# print(x) 

# f = open("emp.py", "r")
# print(f)
# text = f.read()
# print(text)
# f.close()  

# f = open('emp.py', 'w')
# f.write('hello world!')
# f.close 
 
# with open('emp.py', 'w')as f:
#     f.write("Hey i am inside with") 

# f = open('emp', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break 
 
# with open("emp.py", "r") as f:
#     print(type(f))

#     f.seek(10)
#     print(f.tell())
#     data = f.read(5)
#     print(data) 

# with open('emp.py', 'w') as f:
#     f.write('Hello world')
#     f.truncate(5)
 
# with open('emp.py', 'r') as f:
#     print(f.read()) 

######  unit - 2  ####### 

# def double (x):
#     return x*2
# print(double(5)) 

# double = lambda x: x*2 
# print(double(5)) 

# cube = lambda x: x*x*x 
# print(cube(5))

# square =lambda x: x*x 
# print(square(4)) 

# avg = lambda x, y, z:(x+y+z)/3
# print(avg(3, 5, 10))

# def appl(fx, value):
#     return 6+fx(value) 
# print(appl(cube, 2)) 
# print(appl(lambda x: x*x*x, 2)) 

# def cube(x):
#     return x*x*x 
# print(cube(2)) 

# l = [1, 2, 3, 4, 5, 6, 3]
# # newl = []
# # for item in l:
# #     newl.append(cube(item)) 
# # print(newl) 

# newl = list(map(cube, l))
# print(newl)
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x%2 == 0, numbers))
# print(even_numbers)

# def filter_function(a):
#     return a>4 
# newnewl = list(filter(filter_function, l))
# print(newnewl)

from functools import reduce 
numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x+y
sum = reduce(mysum, numbers) 
print(sum) 

# a = 4 
# b = 4 
# a = [1, 2, 44]
# b = [1, 2, 44]
# print(a is b)
# print(a == b)
def hello():
    print("hello")
hello() 

class person:
    name = "ayush"
    occupation = "software developer"
    networth = 50000000000000000000000 
    def info(self):
        print(f"{self.name} is a {self.occupation}") 

a = person()
b = person()
a.name = "shubham"
a.occupation = "accountant"

b.name = "nitika"
b.occupation = "emp"

a. info()
b.info() 

class person:
    def __init__(self, n, o):
        print("Hey I am a person ")
        self.name = n 
        self.occupation = o 
    def info(self):
        print(f"{self.name} is a {self.occupation}") 
a = person("Ayush", "Developer") 
b = person("Divya", "Emp")
c = person(1, 2) 
a.info()
b.info()
c.info() 

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs) 
        print("Thanks for using this function") 
    return mfx 
@greet 
def hello():
    print("Hello world!")

@greet 
def add (a, b):
    print(a+b) 

hello()
add(1, 2) 

class Myclass:
    def __init__(self, value):
        self._value = value 
    def show(self):
        print(f"values is {self._value}") 
    @property 
    def ten_value(self):
        return 10*self._value 
    
    @ten_value.setter 
    def ten_value(self, new_value):
        self._value = new_value/10 

obj = Myclass(10)
obj.ten_vlaue = 47 
print(obj.ten_value)
obj.show()  

class employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id 
    def showdetails(self):
        print(f"The name of employee:{self.id} is {self.name}") 
    
class programmer(employee):
    def showlanguage(self):
        print("The defult languaue is python")

e1 = employee("Rohan Das", 420)
e1.showdetails()
e2 = programmer("nandan", 345)
e2.showdetails()
e2.showlanguage() 

class Employee:
    def __init__(self):
        self.__name = "nitu"

a = Employee()
print(a._Employee__name)  
print(a.__dir__()) 

class student:
    def __init__(self):
        self._name = "nitu"

    def _funname(self):

        return "pyhtonclasses"

class subject(student):

    pass 

obj = student()
obj1 = subject()

print(obj._name)
print(obj._funname())

print(obj1._name)
print(obj1._funname()) 

class math:
    def __init__(self, num):
        self.num = num 

    def addtonum(self, n):
        self.num = self.num+n 

    @staticmethod
    def add(a, b):
        return  a+b 
result = math.add(1, 2)
print(result)
a = math(5)
print(a.num) 
a.addtonum(6) 
print(a.num) 

print(a.add(7, 2))

class employee:
    companyName ="Google"
    def __init__(self, name):
        self.name = name 
        self.raise_amount = 0.02
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = employee("niraj")
emp1.raise_amount = 0.3 
emp1.companyName = "Google india"

emp1.showdetails()
employee.companyName = "apple" 
print(employee.companyName)
emp2 = employee("rohan")
emp2.companyName = "nvidia"
emp2.showdetails() 

class employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
e1 = employee("akash", 12000)
print(e1.name)
print(e1.salary)

string = "ashis -12000"
e2 = employee.fromstr(string) 
print(e2.name)
print(e2.salary) 

# class person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
#         self.vaersion = 1
# p = person ('tom', 30)
# print(p.__dir__)

# print(help(person)) 

class parentclass:
    def parent_method(self):
        print("This is the parent method") 

class childclass(parentclass):
    def parent_method(self):
        return super().parent_method()
    def child_method(self):
        print("This is the child method")
        super(). parent_method ()

child_object = childclass()
child_object.child_method()
child_object.parent_method 

class employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id 
class programmer(employee):
    def __init__(self, name, id, lang):
        super(). __init__(name, id, )
        self.lang = lang 
rohan = employee("Rohan Das", 420)
ayush = programmer("ayush", "2325", "pyhton")
print(ayush.name)
print(ayush.id)
print(ayush.lang) 

class employee:
    def __init__(self, name):
        self.name = name 

    def __len__(self):
        i = 0
        for c in self.name: 
            i = i+1
        return i 
    
e = employee("ayush")
print(e.name)
print(len(e)) 

class shape:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def area(self):
        return self.x *self.y 
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius 
        super().__init__(radius, radius)

    def area(self):
        return 3.14 *self.radius * self.radius 
        # return 3.14 * super().area() 
rec = shape(3, 5)
print(rec.area()) 
    
# c = circle(5)
# print(c.area) 

class vector:
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j 
        self.k  = k 

    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}k"
    def __add__(self, x):
        return vector(self.i + x.i, self.j+x.j, self.k+x.k)

v1 = vector(3, 5, 6)
print(v1)
v2 = vector(1, 2, 9)
print(v2)
print(v1 + v2)
print(type(v1 + v2)) 

class animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species 
    def make_sound(self):
        print("sound made by the animal") 
class Dog(animal):
    def __init__(self, name, bread):
        animal.__init__(self, name, species = "Dog") 
        self.bread = bread 

    def make_sound(self):
        print("Bark") 
d = Dog("Dog", "Dogesh")
d.make_sound() 

a = animal("Dog", "dog") 
a.make_sound() 

class employee:
    def __init__(self, name):
        self.name = name 
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance 
    def show(self):
        print(f"The dance is {self.dance}") 
class Danceremployee(employee, Dancer):
    def __init__(self, dance, name):
        self. dance = dance 
        self.name = name 
o  = Danceremployee("kathak", "shivani")
print(o)
print(o.name)
print(o.dance) 
o.show()
print(Danceremployee.mro())  
 
class animal:
    def __init__(self, name, species):
        self.name = name 
        self.species  = species 
    def show_details(self):
        print(f"name;{self.species}")
        print(f"species:{self.species}") 

class Dog(animal):
    def __init__(self, name, breed):
        animal. __init__ (self, name, species = "Dog")
        self.breed = breed
    def show_details(self):
        animal.show_details(self)
        print(f"breed:{self.breed}") 

class Golderetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Goldenretriever")
        self.color = color 
    def show_details(self):
        Dog.show_details(self)
        print(f"color:{self.color}") 

o = Golderetriever("tomy", "black") 
o.show_details()

# time  module 
# import time 
# def usingwhile():
#     i = 0 
#     while i<2000 :
#         i = i+1 
#         print(i) 

# def usingfor():
#     for i in range(2000):
#         print(i)

# init = time.time()
# usingfor() 
# t1  = time.time() -init 
# init = time.time()
# usingwhile()
# print(t1) 
# print(time.time()- init) 

import time 
# print(4)
# time.sleep(3) 
# print("This is printed after 3 secind. ") 
 
# t = time.localtime()
# formatted_time = time.strftime("%Y_%M_%D" %:%M:%S, t)
# print(formatted_time) 

# a = True 
# print(a:=False) 

# numbers   = [1, 2, 3, 4, 5] 
 
# while len(numbers) > 0:
#     print(numbers.pop())

# happy = True
# print(happy) 
# print(happy := True) 

foods = list() 
while True:
    food = ("wheet")  
     
    if food == "quit":
        break 
    foods.append(food) 

food = list() 
while (food:= "mango")!="quit":
    foods.append(food )'''

