print("hello world ")
print( "Hey I am ayush ") 
print("And my hobies are play cricket ") 
a=123454  
print(a) 
b= 1234 
print(b) 
print(a+b) 
a=20 
b=300 
print("The value of",a ,"+" ,300 ,"is:", a+b)   
print("The value of",a ,"-" ,300 ,"is:", a-b)  
print("The value of",a ,"*" ,300 ,"is:", a*b)  
print("The value of",a ,"/" ,300 ,"is:", a/b) 
name="ayush" 
friend ="Tom" 
anotherfriend= "sarry" 
apple= 'hesaid', "I want to eat food" 
print(name)   
print(friend) 
print(anotherfriend) 
print("hello" + friend) 
niraj='''He said,
Hi ayush
Hey I am good 
"I wanted to eat an apple'''
print(niraj) 
print(name[0]) 
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[4]) 
print("lets use a for loop\n") 
for character in apple: 
    print(character) 
names="niraj", "niraj"
print(names[0:5]) 
fruit="mango"
len1=len(fruit) 
print("mango is a", len1, "letter word") 
print(fruit[0:4]) 
exist="Graps" 
print(len(exist)) 
print(exist[0:4]) 
print(exist[1:4]) 
print(exist[2:4]) 
print(exist[3:4]) 
print(exist[0:-3]) 
print(exist[-3:-1]) 

#quick quize 
nm="niraj" 
print(nm[-4:-2]) 
# THE STINGS ARE IMMUTABLE 
a="niraj"  
print(len(a)) 
print(a.upper()) 
print(a.lower()) 
b="sarry!!!!!!!!!!!!!!"
print(b.rstrip("!")) 
c="jarry!!!!!!!!"
print(c) 
print(c.replace("jarry", "sarry"))  
print(c.split("  ")) 
vlogheading="intoduction to ayush" 
print(vlogheading.capitalize) 
str="I am happy" 
print(len(str)) 
print(len(str.center(50))) 
print(a.count("niraj")) 
str1="welcome to my house" 
print(str1.endswith("to")) 
str1="He is fine" 
print(str1.find("is")) 
print(str1.index("is")) 
str1="welcome" 
print(str1.isalpha()) 
str1="welcometotheconsole" 
print(str1.isalnum()) 
str1="hello world" 
print(str1.islower()) 
str1="HELLO WORLD" 
print(str1.isupper()) 
str1="welcome to my house" 
print(str1.isprintable()) 
str1="      "    "      "  #niraj 
print(str1.isspace()) 
str1="world health organization"
print(str1.istitle()) 
str1="world health organization"  
print(str1.startswith("world")) 
str1="welcome to my house" 
print(str1.swapcase())
str1="welcome to my house "
print(str1.title()) 

 #if elses condition 
 # conditionaloperators
 # >,<, >=, <=, == !=

applesprice=210
budget=200
if(applesprice<= budget): 
    print("alexa, add 1kg apples to the cart.") 
else:
    print("alexa, do not add apples to th e cart.")     



applesprice=10
budget=200
if(budget-applesprice > 50):
    print("alexa, add 1kg apples to the cart. ") 
elif(budget-applesprice > 70 ):
    print("its okay you can buy ") 
else:
    print("alexa, do not add apples to the cart.")         

a = 18
print(a > 18) 
print(a <= 18) 
print(a == 18) 
print(a != 18) 
if(a>18):
    print(" you can drive")
else:
    print("you can not drive ") 


num = 8
if(num<0):
    print("Number is negative.") 
elif(num==0):
    print("Number is zero") 
elif(num==999):
    print("Number is special.") 
else:
    print("Number is positive.") 

    print("I am happy now.") 

num = 15
if(num<0):
    print("Number is negative ") 
elif(num>0):
    if(num<= 10):
        print("Number is between 1-10") 
    elif(num> 10 and num<=20):
        print("Number is between 11-20") 
    else:
        print("Number is greater than 20") 
else:
    print("Number is  zero") 

import time 
timestamp=time.strftime('14:20:40') 
print( timestamp) 
timestamp=time.strftime('14') 
print(timestamp) 
timestamp=time.strftime('20') 
print(timestamp) 
timestamp=time.strftime('40') 
print(timestamp) 
name = 'Ayush' 
for i in name:
    print(i) 
    if(i == "b"): 
        print(" This is something specisl!") 

colors = ["Red", "Green", "Blue", "Yellow"] 
for color in colors: 
    print(color) 
    for i in color:
        print(i) 

for k in range(5): 
    print(k+1) 

for k in range(1, 20001):
    print(k) 

for k in range(1 , 12, 3):
    print(k) 

i = 0
while(i<=3):
    print(i) 
    i=i+1

print("Done with a loop")     

# i= 38
# while(i<=38):
#     print(i)  

print("Done with a loop") 

count = 5
while(count > 0):
    print(count)  
    count = count-1
else:
    print("I am inside else") 

for i in range(12):
    print("5*", i+1, "=", 5 * (i+1)) 
    if(i == 10):
        break 
print("loop ko cjodkar nikal gaya") 

for i in range(12):
    if(i == 10):
        print("skip the interation ") 
        continue 
    print("5*", i+1, "=", 5*(i+1)) 

# i = 0 
# while True: 
#     print(i) 
#     i = i+1 
#     if(i%100 == 0):
#         break  
def calculateGmean(a, b):
    mean = (a*b)/(a+b) 
    print(mean) 
def isgreater(a, b):

  if(a>b):
      print("first number is greater") 
  else:
      print("second number is greater or equal") 
def islesser(a, b):
    pass 

a = 9
b = 8 
isgreater(a, b) 
calculateGmean(a, b) 

def average(a=5, b=7):
    print("The average is", (a+b)/2) 

average(4, 6) 
average(b=9, a=21) 
def average(a, b, c=1):
    print("The average is", (a+b+c)/3) 

average(5, 6) 
def average(*numbers):
    print(type(numbers)) 
    sum=0
    for i in numbers:
        sum=sum+1
    print("Average is:", sum/len(numbers)) 
    return sum/ len(numbers) 

c= average(5, 6, 7, 1) 
print(c) 

def name(**name):
    print(type(name)) 
    print("Hello", name["fname"], name["mname"], name["lname"]) 
name(mname = "buchman", lname = "barnes" ,fname = "janis")
marks = [3, 5, 6, "ayush", True, 23, 45, 678, 56, 34, 12] 
print(marks)
print(type(marks)) 
print(marks[0]) 
print(marks[1]) 
print(marks[2]) 
print(marks[3]) 
print(marks[4]) 
print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive index
print(marks[5-3])
print(marks[2]) 
if 7 in marks:
    print("yes") 
else:
    print("no") 
if "ush" in "ayush":
    print("yes") 
else:
    print("no") 
#same thing applies starting as well! 
print(marks[1:8]) 
print(marks[1:8:3]) 
lst = [i*i for i in range(10)] 
print(lst)
lst = [i*i for i in range(10)if i%2==0]
print(lst) 
l = [23, 1, 2, 2, 3, 4,] #list method
print(l) 
l.append(7)
print(l) 
l.sort(reverse = True) 
print(l) 
l.reverse()
print(l.index(1)) 
print(l) 
print(l.count(2)) 
m = l.copy() 
m[0] = 0
print(l) 
l.insert(1, 45) 
print(l)
m = [900, 1000, 1100] 
l.extend(m) 
print(l)
tup = (1, 5, 6, 56, "yellow") 
print(type(tup), tup) 
print(tup[0]) 
print(tup[1])
print(tup[2]) 
if 56 in tup:
    print("yes 56 is present in this tuple") 
tup2 = tup[1:4] 
print(tup2) 
tuple3 = (0, 1, 2, 3, 4, 3, 5, 3, 6, 3)
res = tuple3.count(3) 
res = tuple3.index(3, 4, 8) 
res = len(tuple3) 
print('count of 3 in tuple:', res) 
# exercise- 2
import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
hour = 22
print(hour) 

if(hour>=0 and hour<12):
    print("Good Morning sir!") 
elif(hour>=12 and hour<17):
    print("Good afternoon sir!") 
elif(hour>=17 and hour<24):
    print("Good night sir!") 
# fstring
letter = "Hey my name is {0} and i am form {1}"
name = "aysuh" 
country = "india" 
print(letter.format(name, country)) 
print(f"Hey my name is {name} and i am form {country}") 
price = 49.09999
txt = f"for only{price:.2f} dollors!" 
print(txt) 
print((f"{2*40}")) 

def square(n):
    '''Takes in a number n, return the square of n'''
    print(n**2) 
square(5) 
print(square.__doc__) 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 
    
print(factorial(5))  
#set method 
s = {2, 4, 2, 6} 
print(s) 
s = {"ayush", "niraj", 5, 6, 7, 7, 6} 
print(s) 
ayush = set()
print((ayush)) 
for value in s:
    print(value) 
s1 = {1, 2, 5, 6} 
s2 = {3, 6, 7} 
print(s1.union(s2)) 
print(s1, s2) 
cities = {"tokyo", "madrid", "berlin", "delhi"} 
cities2 = {"tokyo", "seoul", 'kabul', "madrid"} 
cities3 = cities.union(cities2) 
# cities3 = cities.intersection(cities2)  
# cities3 = cities.symmetric_difference(cities2) 
# cities3 = cities.difference(cities2) 
# cities3 = cities.issuperset(cities2) 
# cities3 = cities.unionisdisjoint(cities2) 
# cities3 = cities.issubset(cities2) 
print(cities3) 
cities = {"tokyo", "madrid", "berlin", "delhi"}
cities.add("maskow") 
print(cities)
# cities.remove("tokyo")
cities = {"Tokyo", "madrid", "berlin", "delhi"} 
item = cities.pop()
print(cities)
print(item) 
# dictionary method
dic = {
    "ayush":"Human being",
    "spoon":"object"
}

print(dic["ayush"])
info = {"name":'ayush', "age":15, "eligable":"true"}
print(info) 
print(info["name"]) 
print(info.get("name")) 
print(info.keys())
print(info.values()) 

for key in info.keys():
    print(info[key]) 

for key in info.keys():
    print(f"The value corresponding to the key{key} is{info[key]}") 

print(info.items()) 
for key, value in info.items():
    print(f"The value corresponding to the key{key} is {value}") 
ep1 = {122:45, 123:89, 567:69, 670:69} 
ep2 = {122:67, 566:90} 
# ep1.update(ep2) 
# ep1.clear()
# ep1.pop(122) 
ep1.popitem()
print(ep1) 
#for loops with esle in pyhon 
for i in[]:
    print()

else:
    print("sorry no i") 
for i in range(6):
    print(i) 
    if i == 4:
        break 

else:
    print("sorry no i") 

i = 0
while i<7:
    print(i)
    i = i+1
    if i ==5:
        break 

else:
    print("sorry no i ") 

for x in range(5):
    print("interation on {} in for loop".format(x+1))
else:
    print("else block in loop") 
print("out of loop") 

a = 4 #ayush
print("Multiplication table of {a} is: ") 
# try:
for i in range(1, 11):
    print(f"{int(a)}x{i} = {int(a)*i}") 
# except Exception as e:
    #print("sorry some error occured") #check

print("some lmp lines of code") 
print("end of programe") 
try:
    num = 1
    a = [6, 3] 
    print(a[num]) 
except ValueError:
    print("number entered is not integer.") 
except IndexError:
    print("index error") 

def func1():
    try:
        l = [1, 5, 6, 7] 
        l = 1
        print(l[i]) 
        return 1
    except:
        print("some error occured") 
        return 0 
    
    finally:
        print("I am always excuted") 

x = func1() 
print(x) 

# a = 4

# if(a<9 or a>9):
#     raise ValueError("value should be between 5 and 9")   
 
"KBC programe" 
questions = ["which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
           ],
["which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
 ],
[ 
    "which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
], 

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000] 
for i in range(0, len (questions)):
    question = questions[i]
    print(f"questions for Rs. {levels[i]}") 
    print(f"a.{questions[i][1]}    b.{questions[i][2]}") 
    print(f"a.{questions[i][3]}    b.{questions[i][4]}") 
    reply = 1, 2, 3, 4 
    if reply == question[-1]:
        print(f"correct answer, you have won Rs.{levels[i]}") 
        if(i == 4):
            money = 10000
        elif(i ==9):
            money = 320000
        else:
             print("wrong answwer!") 
             break  

a = 33 
b = 3303
print("a") if a<b else print("=") if a==b else print("b") 
c = 9 if a<b else 0
print(c) 
marks = {12, 56, 32, 12, 98, 12, 45, 1, 4} 
index = 0
for mark in marks:
     print( mark ) 
     if(index == 3):
            print("jarry, awesome!") 
     index +=1

for index, mark in enumerate(marks, start = 3):
    print(mark)
    if(index == 3):
        print("jarry, awesome") 

###### import type programe 
import math 
math.floor(4.2343) 

result = math.sqrt(9) 
print(result) 
from math import sqrt, pi

result = math.sqrt(9)* pi
print(result) 
import math as m 
result = m.sqrt(9)*m.pi 
print(result) 
import math
print(dir(math)) 
print(math.nan, type(math.nan)) 

import math as math_builtin_python
result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result) 

# from BasicPython import welcome, BasicPython
# from BasicPython import *
# import math 

# print(dir(math)) 
# print(math.nan, type(math.nan)) 
# welcome()
# print(BasicPython) 

# import BasicPython 

# BasicPython.welcome 
#second file jisase file import karana hai vaha likahana hai##
# def welcome():
#     print("Hey you are welcome my friend.") 
# BasicPython = "A good boy" 
# print(__name__)
# if __name__ == "__main__" : 
#     welcome() 

# import os 

# if(not os.path.exists("data")):
#     os.mkdir("data") 
    
# for i in range(0, 100):
#     os.mkdir(f"data/day{i+1}") 
#     os.rename(f"data/day{i+1}", f"data/ayush{i+1}") 


# import os
# folders = os.listdir("data") 


# print(folders) 
# print(os.getcwd())
# os.chdir("/users") 
# print(os.getcwd()) 


# for folder in folders:
#     print(folder) 
#     print(os.listdir(f"data/{folder}")) 
#global and local veribales 
x = 4 
print(x) 

def hello():
    x = 5

    print(f"The local x is {x}") 
    print("Hello ayush") 

print(f"The global x is {x}") 

x = 10 

def my_function():
    global x 
    x = 4 
    y = 5
    print(y) 

my_function()
print(x) 

# f = open('emp ', 'r')   
# print(f) 
# text = f.read() 
# print(text) 
# f.close() 

# f = open('emp ', 'w' ) 
# f.write('Hello world!') 
# f.close()
 
# with open('emp ', 'w')as f:
#     f.write("Hey i am inside with") 

# f = open('emp' 'r') 
# while True:
#     line = f.readline() 
#     print(line) 
#     if not line:
#         print(line, type(line)) 
#         break 

# # f = open('emp', "r") 
# # i = 0
# # while True:
# #     i = i+1
# #     line = f.readline() 
# #     if not line:
# #         break 
# #     m1 = line.split(" , ")[1] 
# #     m2 = line.split(" , ")[2]
# #     m3 = line.split(" , ")[3] 
# #     print(f"marks of student {i} in maths is:{m1}") 
# #     print(f"marks of student {i} in english is:{m2}") 
# #     print(f"marks of student {i} in sst is:{m3}") 

# f = open('emp', 'w' ) 
# lines = ["line1\nline2\nline3\n"] 
# f.writelines(lines) 
# f.close() 
# #day(50) completed 
