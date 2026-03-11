Exercise = 1 
a=20 
b=300 
print("The value of",a ,"+" ,300 ,"is:", a+b)   
print("The value of",a ,"-" ,300 ,"is:", a-b)  
print("The value of",a ,"*" ,300 ,"is:", a*b)  
print("The value of",a ,"/" ,300 ,"is:", a/b) 

Exercise = 2 
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

Excerise = 3 
"KBC programe" 
questions = ["which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
           ],
["which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
 ],
["which language was used to create fb?", "python", "french", "javascript", "php", "none", 4
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
        
b = "Hello, world!" 
# HeLLo world!
c = b.lower()
d = c[2:4] 
e = d.upper()
f = c[:2] + e +c[4:]
print(f)  

x = "Hello, universe!" #create the uper case in univer
y = x.lower() 
t = y[7:13]
e = t.upper()
f = y[:7]+ e + y[13:] 
print(f) 

a = "welcome to my house"  # create hamko only to ko big letter mai chahiye 
b = a.lower()
v = b[8:10]
t = v.upper()
f = b[:8] + t + b[10:]
print(f) 

a = " world trade organization, yah janeva mai hai" # ane upper case 
b = a.lower()
c = b[32:35]
d = c.upper()
g = b[:32] + d + b[35:]  
print(g) 
 
a = "Tom is my friend, and he is living in america inside the florida" # meric ko captial mai change kero 
b = a.lower()
c = b[39:44]
d = c.upper()
e = b[:39] + d + b[44:]
print(e) 

# upper case to lower case 
a = "WHO WAS THE FIRST PRIME MINISTER OF INDIA " # create in lower case in ister 
b = a.upper()
c = b[27:32]
d = c.lower()
e = b[:27] + d + b[32:]  
print(e)  

a = "MR. PANDIT JAWHAR LAL WAS THE FIRST PRIME MINISTER OF INDIA " # create rim and ndi in lower case 
b = a.upper()
c = b[37:40 ] 
d = b[55:58] 
e = c.lower() 
g = d.lower() 
f = b[:37] + e +b[40:55] + g + b[58:]  
print(f)    


a = "MUMBI IS THE FINCIAL CAPTIAL OF INDIA AND DELHI IS THE CAPITAL OF INDIA AND PATANA IS SAME AS BIHAR " 
# INCIAL , ELH ,PITA , PATANA 
b= a.upper() 
c = b[14:20] 
d = b[43:46] 
e = b[57:61] 
f = b[76:82]
g = c.lower()
h = d.lower()
i = e.lower()
j = f.lower() 
k = b[:14] + g + b[20:43] + h + b[46:57] + i + b[61:76] + j + b[82:] 

Exercise =5
import random 
def check(comp, user):
    if comp ==user:
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    
    return 1 

comp = random.randint(0, 2) 
user =  2                          #int(input("0 for snake, 1 for water and 2 for Gun\n")) 

score = check(comp, user) 

print("you:", user)
print("computer:", comp) 

if(score == 0):
    print("its a draw") 
elif (score==-1): 
      print("You lose")  
else:
    print("You won") 

Excerise = 6 
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
EXriecise = 7 
# import os

# files = os.listdir("clutteredfolder") 
# for file in files:
#     print(files) 

# # os.rename("clutteredfolder/file.txt", "clutteredfolder/6.txt") 
# import os
