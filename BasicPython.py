print("hello world") 
print("hey i am ayush ")
print("and my hobies are play cricket ") 
a=123432232
print(a)
b= 234545332 
print(b) 
print(a+b) 
a=20
b=200

print("The value of",a , "+" ,200 , "is:", a+b) 
print("The value of",a , "-" ,200 , "is:", a-b) 
print("The value of",a , "*" ,200 , "is:", a*b) 
print("The value of",a , "/" ,200 , "is:", a/b) 
name ="ayush" 
friend= "prabhat" 
anotherfriend="nirsj"
apple= 'He said,' "I want to eat an apple " 
print("apple") 
print(apple)
print(name) 
print(friend) 
print(anotherfriend) 
print("hello," + name) 
bikash= '''he said ,
Hi prabhat 
Hey i am good 
"I want to eat food '''
print(bikash) 
print(name[0]) 
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[4]) 
print("lets use a for loop \n")
for character in  apple: 
    print(character) 
names="carry ,nirsj"
print(names[0:5]) 
fruit ="mango" 
len1= len(fruit)  
print("mango is a", len1, "letter word.") 
print( fruit [0:4])  
exist="Graps" 
print(len(exist)) 
print(exist[0:4]) 
print(exist[1:4]) 
print(exist[2:4]) 
print(exist[3:4])  
print(exist[0:-3])   
print(exist[-3:-1])     
    
#Quick quize 
nm= "carry" 
print(nm[-4:-2])
# Thesrings are immutable
a="carry"
print(len(a)) 
print(a.upper()) 
print(a.lower()) 
b="sarry!!!!!!!!!!!!!!!!!"
print(b.rstrip("!")) 
c="jarry!!!!!!!!!"  "jain"
print(c) 
print(c.replace("jarry", "sarry")) 
print(c.split(" ")) 
vlogheading="introduction to bs" 
print(vlogheading.capitalize()) 
str= "I am happy"
print(len(str)) 
print(len(str.center(50))) 
print(a.count("carry")) 
str1 = "welcome to my house" 
print(str1.endswith("to")) 
str1="He is fine"
print(str1.find("is")) 
print(str1.index("is")) 
str1="Welcome" 
print(str1.isalpha()) 
str1="Welcometotheconsole"
print(str1.isalnum()) 
str1="hello world"
print(str1.islower()) 
str1="HELLO WORLD"
print(str1.isupper()) 
str1="welcome to my house "
print(str1.isprintable()) 
str1="           "               #carry
print(str1.isspace()) 
str1="world health organization" 
print(str1.istite()) 
str1="world health organization" 
print(str1.startswith("world")) 
str1="welcome to my house" 
print(str1.swapcase()) 
str1="welcome to my house" 
print(str1.title()) 
# if else condition 
# conditional operators 
# >,<,>=,<=, == != 

appleprices=210
budget =200
if(appleprices<= budget): 
    print("Alexa, add 1kg applesto the cart.") 
else:
    print("Alexa, do not add applesto the cart.") 

   

applesprice =10
budget =200
if(budget- applesprice > 50): 
    print("alexa, add 1kg apples to the cart. " )
elif(budget-applesprice>70):
    print("Its okay you can buy ")      
else:
    print("alexa, do not add apples to the caart. ") 


name='Ayush'
for i in name:
    print(i)
    if(i == "b"):
        print("This is something special!") 

colors = ["Red", "Green", "Blue", "Yellow"] 
for color in colors:
    print(color)
    for i in color:
        print(i) 

for k in range(5):
    print(k+1) 

# for k in range(1, 20001): 
    # print(k) 

for k in range(1, 12, 3):
    print(k)  
    

i=0
while(i<=3):
    print(i) 
    i=i+1 

print ("Done with a loop") 


# i= int(input("Enter the number: ")) 
# while(i<=38): 
#     i=int(input("Enter the number: ")) 
#     print(i) 

# print("done with the loop ") 

count = 5
while(count > 0): 
    print(count) 
    count = count-1 
else:      
    print("I am inside else ")  


for i in range(12):
    print("5*", i+1, "=", 5 * (i+1 )) 
    if(i == 10):
      break
print("loop ko chodkar nikal gaya") 


for i in range(12): 
    if(i == 10):
        break 
    print("5*", i+1, "=", 5* (i+1)) 
print("loop ko chodkar nikal gaya") 

    
for i in range(12):
    if(i == 10):
      print("skip the iteration") 
      continue 
    print("5*", i+1, "=", 5*(i+1) )          


# i = 0 
# while True:
#     print(i) 
#     i = i+1  
#     if(i%100 == 0):
#         break  
    
def calculateGmean(a ,b):
    mean = (a*b)/(a+b) 
    print(mean) 
def isGreater(a, b):

  if(a>b):
    print("first number is greater" ) 
  else:
    print("second number is greater or equal") 
def islesser(a, b): 
    pass 
 
a = 9 
b = 8
isGreater(a ,b) 
calculateGmean(a, b) 
gmean1 = (a*b)/(a+b) 
print(gmean1) 
c = 8
d = 71
if(c>d):
    print("first number is greater") 
else:
    print("second number is grester or equal") 

calculateGmean(c, d)    
gmean2 = (c*d)/(c+d)  
print(gmean2) 

def average(a=5, b=7):
    print("The average is", (a+b)/2) 

average(4, 6) 
average(b=9, a=21) 
def average(a, b, c=1): 
    print("The average is", (a+b+c)/2) 

average(5, 6) 
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:", sum/len(numbers)) 
    return sum/ len(numbers) 


c= average(5, 6, 7, 1) 
print(c) 
def name(**name): 
    print (type(name))
    print("Hello,",name["fname"], name["mname"], name["lname"]) 

name(mname ="buchman", lname = "barnes", fname = "james")
marks=[3, 5, 6, "ayush", True, 23, 45, 678, 56, 34, 12]   
print(marks) 
print(type(marks)) 
print(marks[0]) 
print(marks[1]) 
print(marks[2]) 
print(marks[3]) 
print(marks[4])  
print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive index
print(marks[5-3]) #positive index 
print(marks[2]) #positive index 
if 7 in marks:
    print("yes") 
else:
    print("no") 
if "ush" in "ayush":
    print("yes")
#  same thing applies for string as well!
print(marks) 
print(marks[1:8]) 
print(marks[1:8:3]) 
lst = [i*i for i in range (10)]  
print(lst) 
lst = [i*i for i in range(10) if i%2==0] 
print(lst) 
l=[23, 1, 2, 2, 3, 4] #list method 
print(l) 
l.append(7)
print(l) 
l.sort(reverse = True )  
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
print('count of 3 in tuple3:', res) 
#excerise 2

# def welcome():
#     print("Hey you are welcome my friend") 
# BasicPython  = "A good boy" 
# print(__name__) 
# if __name__ == "__main__":  
#     welcome() 

