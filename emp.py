# print("Hello world") 
# a = "ayush"
# b = "welcome"
# print(a + b) 
# c = "10" 
# d = "10" 
# print(c + d ) 
# x = 3.5 
# y = 4.5 
# print("The value of",x , "+", y, "is:", x+y)
# print("The value of",x , "-", y, "is:", x-y)
# print("The value of",x , "*", y, "is:", x*y)
# print("The value of",x , "/", y, "is:", x/y) 
# lst = [1, 2 , 3, 4, 5]
# lst1 = ["a", "b", "c", "d"] 
# print(type(lst))
# print(type(lst1)) 

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3) 


# Basic Python For Loop Questions (Class 11)
# Q1. Write a program to print numbers from 1 to 10 using a for loop.
# Q2. Write a program to print all even numbers between 1 and 20 using a for loop.
# Q3. Write a program to print all odd numbers between 1 and 20 using a for loop.
# Q4. Write a program to print the multiplication table of a given number using a for loop.
# Q5. Write a program to calculate the sum of first 10 natural numbers using a for loop.
# Q6. Write a program to find the factorial of a number using a for loop.
# Q7. Write a program to print each character of a string using a for loop.
# Q8. Write a program to count the number of characters in a string using a for loop.
# Q9. Write a program to print the square of numbers from 1 to 10 using a for loop.
# Q10. Write a program to display the following pattern using a for loop: * ** *** ****



# Q1. Write a program to print numbers from 1 to 10 using a for loop.
'''list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

for i in list: 
    print(i)  

for x in range(1, 11):  
    print(x) 

# Q2. Write a program to print all even numbers between 1 and 20 using a for loop.
    

for i in range(1, 21):  
    if(i % 2 == 0): 
        print (i)
    
# Q3. Write a program to print all odd numbers between 1 and 20 using a for loop. 
for i in range(1, 21):  
    if(i % 2!= 0):  
        print (i) 
# Q4. Write a program to print the multiplication table of a given number using a for loop.
for i in range(12):
    print("55*", i, "=", 55 * (i))   
    if(i == 10):      
        break 
num = 6 
for i in range(1, 11):
  print(num, "*", i, "=", i*num)

# Q5. Write a program to calculate the sum of first 10 natural numbers using a for loop.
 
total = 0 
for i in range(1, 51):
    total += i

print("sum of numbers from 1 to 50 is:", total)   



# Q6. Write a program to find the factorial of a number using a for loop. 

 
# Q7. Write a program to print each character of a string using a for loop

text =  "gaurav"                               #input("Enter a string: ")
for x in text:
    print(x)          #chat gtp


# Q8. Write a program to count the number of characters in a string using a for loop

text = "ayush" 

count = 0
for ch in text: 
    count += 1  # chat gtp 

print("Number of characters:", count)
# Q9. Write a program to print the square of numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    # print("Square of", i, "is", i * i)
    print(i*i)   # chat gtp

# Q10. Write a program to display the following pattern using a for loop: * ** *** ****
for i in range(1, 7):
    print("*" *i)  # chat Gtp


# Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:
marks = 85
if marks >90:
    print(" you Got A grade") 
elif marks > 80 and marks <= 90: 
    print("you got B grade")
elif marks >= 60 and marks <= 80:
    print("you got c grade")
else:
    ("you got D grade")
# Q2. Write a program to accept the cost price of a bike and display the road tax to be paid:
costprice = 120000
if costprice >100000:
    print("Bike tax = 15%")
elif costprice >50000 and  costprice <=100000:
    print("Bike tax = 10%")
elif costprice > 30000 and costprice <=50000:
    print("Bike tax = 7%")
else:
    print("Bike tax = 5%")

# Q3. Write a program to check whether a year is leap year or not.
# Q4. Write a program to accept a number from 1 to 7 and display the name of the day.
day = 5 

if day ==1:
    print("Monday")
elif day ==2:
    print("Tuesday")
elif day ==3:
    print("Wensday")
elif day ==4:
    print("Thursday")
elif day ==5:
    print("Friday")
elif day ==6: 
    print("saturday")
else:
    print("Saturday")  
#Q5. Write a program to accept a number from 1 to 12 and display the month name and number of days.
month = 10 
if month ==1:
    print("January")
elif month ==2:
    print("February")
elif month ==3:
    print("March")
elif month ==4:
    print("April")
elif month ==5:
    print("May")
elif month ==6:
    print("June")
elif month ==7:
    print("July")
elif month ==8:
    print("August")
elif month ==9:
    print("September")
elif month ==10:
    print("octover")
elif month ==11:
    print("Novmeber")
else:
    print("December")

x = 10     # assignment statement ## chat Gtp

print(x)     # output statement 
a = 5

# name = input("Enter name:")
# print(name)




if a > 0:
    print("Positive")




for i in range(5):
    print(i)
# Q8. Write the logical expression:
# A is greater than B and C is greater than D
A = 200 
B = 50 
c = 400 
D = 75 
if A > B and c > D:
    print("yes")
else:
    print("No")
#Q9. Accept any city from the user and display monument of that city:
city = "delhi" 
if city == "delhi":
    print("Monument: Red fort")
elif city == "Agra":
    print("Monument: Taj Mahal")
elif city == "Jaipur":
    print("Monument: Jal Mahal")
elif city == "hydrabad":
    print("Monument: char minar")
else:
    ("Monument information is not available")
# Q10. Write the output if a = 9:
a = 9 
if a>5 and a<= 10:
    print("Hello") 
else:
    print("Bye") 

# Q3. Write a program to check whether a year is leap year or not.
# Based on chat gtp
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

string = "ayush"
reverse_str= "" 

for i in string:
    reverse_str = i + reverse_str  
print("reversed string:", reverse_str)     

num = 3                   #int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)
num = 4 
fact = 1 

for i in range(1, num+1):
        fact = fact *i 
print("factriol of", num, "is", fact) 

a = "AEIOU"
count = 0 
for i in a:
    count = count + 1
print("print the vowel =", count) 

for  i in range(10, 0, -1):
    print(i)''' 

x = input("Enter a string:") 
print(x)
