
def my_function():
    print("Hello from a function")

my_function() 

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message) 

def get_greeting():
    return "Hello from a function"

print(get_greeting()) 

def my_function():
    pass 

def my_function(fnmae):
    print(fnmae + " ayush ") 

my_function("name")
my_function("Email")
my_function("password") 

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Email", "refers") 

def my_function(name = "friend"):
    print("Hello", name) 

my_function("Email")
my_function("tobais")
my_function()
my_function("linus") 

def my_function(country = "narway"):
    print("I am from", country)

my_function("sweden")
my_function("India")
my_function()
my_function("Brazil") 

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal +"'s name is", name)

my_function(animal = "dog", name = "Tomy")  

def my_function(name, animal): 
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("buddy", "dog")  

def my_function(animal, name, age):
    print("I have a", animal, "his's name is", name, "and age=", age)

my_function("dog", "Tomy", 4)  

def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "lichi"]
my_function(my_fruits)

def my_function(person):
    print("Name:",person["name"])
    print("age:", person["age"])

my_person = {"name": "Email", "age":16}
my_function(my_person) 

def my_function(x, y):
    return x + y 

result = my_function(5, 3)
print(result) 

def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
for i in fruits:
    print(i) 

def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y) 

def my_function(name, /):
    print("Hello", name)

my_function( "Email") 

def my_function(name):
    print("Hello", name)

my_function(name = "Emial")

def my_function(*, name):
    print("Hello", name)

my_function(name = "Emil") 

def my_function(a, b, /, *, c, d):
    return a + b + c + d 

result = my_function(5, 10, c = 15, d = 20)
print(result) 

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Email", "tobias", "linus") 

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
    
my_function("Hello", "Emil","tobias","linus") 

def my_function(*numbers):
    total = 0 
    for i in numbers: 
        total += i 
    return total 

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40, 50))
print(my_function(5))  

def my_function(*numbers):
    if len(numbers) == 0:
        return None 
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num 
    return max_num 
print(my_function(3, 4, 5, 56, 6, 9, 1)) 
print(my_function(1, 34, 6, 7, 56, 75, 2, 3, 1 ))
print(my_function(23, 1, 3, 4, 6, 7, 90, 2, 3, 5)) 

def my_function(**kid):
    print("His first name is " + kid["fname"]) 

my_function(fname = "aysuh", lname = "sky") 

def my_function(username, **details):
    print("username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
my_function("email123", age = 16, city = "dbg",  hobby = "coding")

def my_function(title, *args, **kwargs):
    print("Title", title)
    print("positional argument:", args)
    print("keyword argunment:", kwargs)

my_function("user info", "Email", "Tobias", age = 25, city = "oslo")

def my_function(a, b,c):
    return a + b + c 
numbers = [1, 2, 3]
result  = my_function(*numbers)
print(result)

def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname":"referse"}
my_function(**person)  

def myfunc():
    x = 300 
    print(x)

myfunc() 

def myfunc():
    x = 300 
    def myinnerfunc():
        print(x)
    myinnerfunc() 

myfunc() 

x = 300 
def myfunc():
    print(x)

myfunc()
print(x) 

x = 300 
def myfunc():
    x = 200 
    print(x)

myfunc()
print(x) 

def myfunc():
    global x 
    x = 300 
myfunc()
print(x)  

x = 300 
def myfunc():
    global x 
    x = 200 
myfunc()
print(x) 

def myfunc1():
    x = "jane"
    def myfunc2():
        nonlocal x 
        x = "Hello"
    myfunc2()
    return x 
print(myfunc1()) 

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x) 


''' decoters '''
def changecase(func):
    def myinner(): 
        return func().upper()
    return myinner 

@changecase 
def myfunction(): 
    return "Hello silly"
print(myfunction()) 

def changecase(func): 
    def myinner():
        return func().upper() 
    return myinner 
@changecase 
def myfunction(): 
    return "Hello silly"  
@changecase 
def otherfunction():
    return "I am alright"
@changecase
def anotherfunction():
    return "welcome to my house"

print(myfunction())
print(otherfunction()) 
print(anotherfunction()) 

def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner 
@changecase 
def myfunction(nam):
    return "Hello" + " " + nam 
print(myfunction("john"))   

def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper() 
    return myinner
@changecase 
def myfunction(nam):
    return "Hello"+ " " + nam 
print(myfunction("john")) 


def changecase(n):
    def changecase(func):
        def myinner():
            if n ==1:
                a = func().lower()
            else:
                a = func().upper()
            return a 
        return myinner 
    return changecase 
@changecase(1)
def myfunction():
    return "Hello linus"
print(myfunction())  

def changecase(func):
    def myinner():
        return func().upper()
    return myinner 
def addgreeting(func):
    def myinner():
        return "Hello" + func() + "Have a good day!"
    return myinner 
@changecase
@addgreeting 
def myfunction():
    return " jonny "
print(myfunction()) 

def myfunction():
    return "Have a great day!"
print(myfunction.__name__)  

def changecase(func):
    def myinner():
        return func().upper()
    return myinner 
@changecase 
def myfunction():
    return "Have a Great day!"
print(myfunction.__name__) 

import functools 
def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner 
@changecase 
def myfunction():
    return "Have a great day!" 
print(myfunction.__name__) 

''' python lambda''' 
x = lambda a: a+10
print(x(5)) 

x = lambda a, b: a*b 
print(x(5, 6)) 

x = lambda a, b, c:a + b +c 
print(x(5, 6, 8)) 

def myfunc(n):
    return lambda a: a*n 
double = myfunc(3)
print(double(11)) 

def nyfunc(n):
    return lambda a: a*n 
doubler = myfunc(2)
tripler = myfunc(3)
print(doubler(11))
print(tripler(11) ) 

numbers = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda x: x*2, numbers))
for i in doubled:
    print(i) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
for i in odd_numbers:
    print(i) 
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_student = sorted(students, key = lambda x: x[1])
print(sorted_student)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key = lambda x: len(x))
print(sorted_words) 
''' recursion '''
def countdown(n):
    if n <= 0: 
        print("Done!")
    else: 
        print(n)
        countdown(n - 1) 
countdown(5) 

def factorial(n):
    if n==0 or n==1:
        return 1 
    else:
        return n* factorial(n - 1)
print(factorial(5)) 

def fibonacci(n):
    if n <= 1: 
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
print(fibonacci(13)) 

def sum_list(numbers): 
    if len(numbers) == 0:
        return 0 
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list)) 

def my_generator():
    yield 1 
    yield 2 
    yield 3 
for value in my_generator():
    print(value) 

def count_up_to(n):
    count = 1 
    while count <=n:
       yield count 
       count +=1 
for i in count_up_to(5):
    print(i) 

def large_squence(n):
    for i in range(n):
        yield i 
gen = large_squence(1000000)
print(next(gen))
print(next(gen))
print(next(gen)) 

def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"
   
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) 

list_comp = [x * x for x in range(5)]
print(list_comp)
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp)) 

total = sum( x * x for x in range(10))
print(total) 

def fibonacci():
    a, b = 0, 1 
    while True:
        yield a 
        a, b = b, a + b 

gen = fibonacci()
for _ in range(100):
    print(next(gen)) 

def echo_generator():
    while True:
        received = yield 
        print("received:", received)
gen = echo_generator()
next(gen)
gen.send("Hello")
gen.send("world") 

def my_gen():
    try: 
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close() 

'''function with practice # 20 program  
# function to print "hello world"'''
def my_function(): 
    return "Hello universe" 
print(my_function()) 
''' function add two numbers:''' 
def my_function(x, y): 
    return x + y 
print(my_function(5,3)) 
''' function subtract two numbers:''' 
def my_function(a, b): 
    return a - b 
print(my_function(7, 6))  
'''function multiply two numbers:''' 
def function(x, y): 
    return x * y 
print(function(123, 345)) 
''' function divided two numbers:'''
def function(x, y ): 
    return x // y 
print(function(34, 17))  
''' function to check even or odd''' 
def function(i): 
    if  i % 2 ==0: 
        return "Even" 
    else: 
        return "odd" 
print(function(4)) 
''' function to find square of a numbers:'''
def function(n): 
    return n* n 
print(function(15))  
''' function to find cube of numbers:''' 
def cube(n): 
    return n ** 3
print(cube(4)) 
'''function to find factriol of numbers:''' 
def function(n): 
    fact = 1 
    for i in range(1, n+1): 
        fact *= i 
    return fact 
print(function(5))   
print(function(4))    
print(function(3))   
print(function(2))   
'''function to check prime numbers:''' 
def function(n): 
    if n <= 1: 
        return "Not prime"
    for i in range(2, n): 
        if n % i ==0: 
            return "Not prime"  
    return "prime" 
print(function(7)) 
''' function to print numbers from 1 to n :''' 
def function(n): 
    for i in range(1, n+1): 
        print(i) 
function(10)      
'''functin to sum of n numbers: '''
def my_function(n): 
    total = 0 
    for i in range(1, n+1): 
        total += i 
    return total 
print(my_function(65))
'''function to check leap year:''' 
def function(year): 
    if year % 400 == 0 or (year % 4 ==0 and year % 100 != 0): 
        return "leap year"
    else:
        return "Not leap year"
print(function(2026))
''' function to reverse a number:''' 
def reverse_number(n): 
    rev = 0 
    while n > 0: 
        rev = rev * 10 + n %10 
        n//= 10 
    return rev 
print(reverse_number(1234)) 

def palindrome(n): 
    return n == reverse_number(n)
print(palindrome(121)) 
''' function to find maximum of two numbers:''' 
def function(a, b): 
    if a > b: 
        return a 
    else: 
        return b 
print(function(8, 5))
print(function(6, 5)) 
'''function count digit of numbers:''' 
def count_digit(n): 
    count = 0 
    while n>0: 
        count += 1 
        n//= 10
    return count 
print(count_digit(45678)) 
''' function to print multiplication table. '''
def table(n): 
    for i in range(1, 11): 
        print(n, "x", i,"=", i*n)
table(6) 
''' function to check positive , negative or zero.''' 
def check_number(n): 
    if n > 0:  
        return "positive"
    elif n < 0: 
        return "negative"
    else: 
        return "zero" 
print(check_number(-3)) 
'''find sum of digit:''' 
def sum_digit(n): 
    total = 0 
    while n > 0: 
        total += n % 10 
        n//= 10 
    return total 
print(sum_digit(1342341))
