 # with open("emp", "r") as f: 
#     print(type(f)) 


    # f.seek(10) 
     
#     print(f.tell()) 
#     data = f.read(5) 
#     print(data) 

# with open('emp', 'w') as f:
#     f.write('Hello world!') 
#     f.truncate(5) 

# with open('emp','r')as f:
#     print(f.read()) 

def double(x):
    return x*2 
print(double(5)) 

double = lambda x: x*2 
print(double(5)) 
cube = lambda x: x*x*x
print(cube(5)) 
avg = lambda x, y, z:(x+y+z)/3
print(avg(3, 5, 10)) 
def appl(fx, value):
    return 6+fx(value) 
print(appl(cube, 2)) 
print(appl(lambda x: x*x*x, 2)) 
#MAP
def cube(x):
    return x*x*x 
print(cube(2)) 

l = [1, 2, 3, 4, 5, 6, 3] 
# newl = []
# for item in l:
#     newl.append(cube(item)) 

# print(newl)
newl = list(map(cube, l)) #lambda x: x*x*x, l#
print(newl)  
#FILTER
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function, l)) 
print(newnewl) 

from functools import reduce
numbers = [1, 2, 3, 4, 5] 

def mysum(x, y):
    return x+y 

sum = reduce(mysum, numbers) 
print(sum) 
# a  =4
# b  ="4" 
a = [1, 2, 44] 
b = [1, 2, 44] 
print(a is b) #exact location of object memory 
print(a == b) #value 
# excerise-5 SNAKE WATER GUN 
 #object oriented
# def hello():
#     print("hello") 

# hello()
# sales1 = 6000
# profit1 = 2000
# ad1 = 1000
# # rajeev.sales

# sales2 = 6000
# profit2 = 2000
# ad2 = 1000
# # vikrant.sales 

# Railwayform   --->class 
# ayush--->ayush ki info wala form-->object[entity] 
# tom--->tom ki info wala form-->object[entity] 
# shubham--->shubham ki info wala form-->object[entity] 
# shubham.changename("shubhi") 

class person:
    name = "ayush"
    occupation = "software developer"  
    networth = 5000000000000000000000000000
    def info(self):
        print(f"{self.name} is a {self.occupation}") 

a = person() 
b = person() 
a.name = "shubham"
a.occupation  = "accountant" 

b.name = "nitika" 
b.occupation = "Emp" 
# print(a.name, a.occuption)  
a.info() 
b.info()  

class person:

    def __init__(self, n, o):  
        print("Hey I am a person") 
        self.name = n
        self.occupation = o

    def info(self):
      print(f"{self.name} is a {self.occupation}") 

a = person("Ayush", "Developer")
b = person("Divya", "Emp") 
c = person(1, 2) 
# print(a.name) 
# a.name = "Divya" 
# a.accupation = "Emp"
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
def add(a, b):
    print(a+b) 

hello() 
# greet(add(1, 2)) 
add(1, 2) 

class Myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"value is {self._value}") 
    @property
    def ten_value(self):
        return 10*self._value 
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
    
obj = Myclass(10) 
obj.ten_value = 47 
print(obj.ten_value) 
obj.show() 

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"The nameof employee:{self.id} is {self.name}") 


class programeer(employee):
    def showlanguage(self):
        print("The default language is python")  

e1 = employee("Rohan Das", 420)   
e1.showdetails()    
e2 = programeer("nandan", 345)
e2.showdetails() 
e2.showlanguage() 

class Employee:
    def __init__(self):
        self.__name = "nitu" 

a = Employee()
# print(a.__name)
print(a._Employee__name) 
print(a.__dir__()) 

class student:
    def __init__(self):
        self._name = "nitu" 

    def _funname(self):

        return "pythonclasses"
    
class subject(student):

    pass 

obj = student() 
obj1 = subject() 

print(obj._name) 
print(obj._funname()) 

print(obj1._name) 
print(obj1._funname()) 
#SNAKE WATER GUN GAME #
# import random 
# def check(comp, user):
#     if comp ==user:
#         return 0
#     if(comp == 0 and user == 1):
#         return -1
#     if(comp == 1 and user == 2):
#         return -1
#     if(comp == 2 and user == 0):
#         return -1
    
#     return 1 

# comp = random.randint(0, 2) 
# user =  2                          #int(input("0 for snake, 1 for water and 2 for Gun\n")) 

# score = check(comp, user) 

# print("you:", user)
# print("computer:", comp) 

# if(score == 0):
#     print("its a draw") 
# elif (score==-1): 
#       print("You lose")  
# else:
#     print("You won") 

## excerise- 6##
#libarary class to generate

class math:
        def __init__(self, num): 
            self.num = num

        def addtonum(self, n):
            self.num = self.num+n

        @staticmethod
        def add(a, b):
            return a+b 
result = math.add(1, 2) 
print(result)  
a = math(5) 
print(a.num) 
a.addtonum(6) 
print(a.num) 

print(a.add(7, 2)) 

class employee:
    companyName = "Google" 
    def __init__(self, name):
        self.name = name 
        self.raise_amount = 0.02
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")  
    
emp1 = employee("niraj") 
emp1.raise_amount = 0.3
emp1.companyName = "Google India" 
# employee.showdetails(emp1)
emp1.showdetails()  
employee.companyName = "apple" 
print(employee.companyName) 
emp2 = employee("rohan") 
emp2.companyName = "nvidia" 
emp2.showdetails() 
#excerise -6 solution 
class library:
    def __init__(self):
        self.noBooks = 0 
        self.books = [] 

    def addbook(Self, book):
         Self.books.append(book) 
         Self.noBooks = len(Self.books) 
    
    def showinfo(self):
        print(f"The library has {self.noBooks} books. The books are ") 
        for book in self.books:
         print(book)  

l1 = library() 
l1.addbook("niraj potter1") 
l1.addbook("niraj potter2") 
l1.addbook("niraj potter3") 
l1.showinfo() 

class employee:
    company = "Google" 
    def show(self):
        print(f"The name is{self.name} and company is {self.company}") 
    
    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany

e1 = employee() 
e1.name = "niraj" 
e1.show()
e1.changecompany("tesla") 
e1.show()
print(employee.company) 

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

# x = [1, 2, 3]
# print(dir(x)) 
# print(x.__dir__) 

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.version = 1 

# p = person('tom', 30) 
# print(p. __dir__)

# print(help(person)) 

class parentclass:
    def parent_method(self):
        print("This is the parent method.") 

class childclass(parentclass):
    def parent_method(self):
        print("ayush") 
        super().parent_method()
    def child_method(self):
        print("This is the child method.") 
        super().parent_method() 

child_object = childclass()
child_object.child_method()
child_object.parent_method  

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id =id 

class programmer(Employee): 
    def __init__(self, name, id, lang):
        # self.name = name
        super().__init__( name, id, ) 
        self.lang = lang

rohan = Employee("Rohan Das",420) 
ayush = programmer("ayush", "2325", "python") 
print(ayush.name)   
print(ayush.id)    
print(ayush.lang) 

# class employee:
#     def __init__(self, name):
#         self.name = name


#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i+1
#         return i
    

# # e = employee("ayush") 
# # print(e.name) 
# # print(len(e)) 

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

    # def area(self):
        # return 3.14 * self.radius * self.radius
    def area(self):
        return 3.14 * super().area() 
# rec = shape(3, 5)
# print(rec.area()) 

c = circle(5) 
print(c.area()) 
# #excerise -7
# import os

# files = os.listdir("clutteredfolder") 
# for file in files:
#     print(files) 

# # os.rename("clutteredfolder/file.txt", "clutteredfolder/6.txt") 
# excerise -8
class vector:
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j 
        self.k = k

    def __str__(self):
        return f"{self.i}i +{self.j}j +{self.k}k"
    def __add__(self, x):
        # return f"{self.i +x.i}i + {self.j+x.j}j + {self.k + x.k}k" 
        return vector(self.i+ x.i, self.j+x.j, self.k+x.k) 
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
    def __init__(self, name, breed):
        animal.__init__(self, name, species ="Dog") 
        self.breed = breed 

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
        self.dance = dance
        self.name = name

o =Danceremployee("kathak", "shivani") 
print(o) 
print(o.name)
print(o.dance) 
o.show() 
print(Danceremployee.mro())  

class animal:
    def __init__(self, name, species):
        self.name = name
        self. species = species
    def show_details(self):
        print(f"name:{self.species}")
        print(f"species: {self.species}") 

class Dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "Dog") 
        self.breed = breed 
    def show_details(self):
        animal.show_details(self) 
        print(f"breed: {self.breed}") 

class Golderetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed = "Goldenretriever") 
        self.color = color 
    def show_details(self):
        Dog.show_details(self) 
        print(f"color: {self.color}") 

o = Golderetriever("tomy", "black") 
o.show_details() 
## hibride intrience##
class baseclass:
    pass
class Derived1(baseclass):
    pass
class Derived2(baseclass):
    pass
class Derived3(Derived1, Derived2 ):
    pass
# excerise -8 solution
 # excerise -9  
 
#time Module
# import time 
# def usingwhile():
#     i = 0
#     while i<50000:
#         i = i+1
#         print(i) 

# def usingfor():
#     for i in range(50000):
#         print(i) 

# init =  time.time() 

# usingfor()
# t1 =  time.time() - init 
# init = time.time()  
# usingwhile() 
# print(t1) 
# print(time.time() - init) 
import time 
print(4) 
time. sleep(3) 
print("This is printed after 3 seconds.")
# t = time.localtime() 
# formatted_time = time.strftime("%Y_%M_%D" %H:%M:%S ,t) 
# print(formatted_time) 

# a = True
# print(a:=False) 

# numbers = [1, 2, 3, 4, 5]

# while (n:= len(numbers)) > 0:
#     print(numbers.pop()) 

# happy = True
# print(happy) 
# print(happpy := True) 

foods = list() 
while True:
    food = ("wheet") 

    if food == "quit":
        break 
    foods.append(food) 

foods = list()
while (food:= "mango")!="quit":
    foods.append(food) 
# from os import system
# names = ["Rahul,", "Rohan", "tom"] 
# for name in names :
#     system (f"say{names}") #day -88 
# request Module
# import requests 
# response = 
# requests.get("https://www.google.com") 
# print(response.text)  
# excerise - 10
# def my_generator():
#     for i in range(5000): 
#         # complex computations
#         yield i
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for j in gen: 
    # print(j) 
# function caching# 
 
import functools
import time

@functools.lru_cache(maxsize=None) 
def fx(n):
    time.sleep(5) 
    return n*5 

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2") 
print(fx(6))
print("done for 6 ") 
#excerise -10 solution 
#excerise- 11 
#regular excepression #
# import re 
# pattern = ""
# text = ''''''
import time 
import asyncio  
async def function1():
    await asyncio.sleep(1) 
    print("func1") 
    return "ayush" 

async def function2():
    await  asyncio.sleep(1)
    print("func2") 

async def function3():
    await asyncio.sleep(4)
    print("func3") 

async def main():
  L = await asyncio.gather( 
            function1(),
            function2(),
            function3(), 
    )
print(l)   
asyncio.run(main()) 

from main import employee 

e = employee("niraj") 
print(str(e))
print(repr(e)) 
e()
#comand line utility




 

        

