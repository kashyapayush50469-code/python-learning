'''import os 

if(not os.path.exists("data")):
    os.mkdir("data") 
    
for i in range(0, 100):
    ## os.mkdir(f"data/day{i+1}") 
    os.rename(f"data/day{i+1}", f"data/Ayush{i+1}")'''

# f = open('filer.py ', 'r')    
# print(f) 
# text = f.read() 
# print(text) 
# f.close() 

# f = open('filer ', 'w' ) 
# f.write('Hello world!') 
# f.close()
 
# with open('filer ', 'w')as f:
#     f.write("Hey i am inside with") 

# f = open('filer' 'r') 
# while True:
#     line = f.readline() 
#     print(line) 
#     if not line:
#         print(line, type(line)) 
#         break 

# f = open('filer', "r") 
# i = 0
# while True:
#     i = i+1
#     line = f.readline() 
#     if not line:
#         break 
#     m1 = line.split(" , ")[1] 
#     m2 = line.split(" , ")[2]
#     m3 = line.split(" , ")[3] 
#     print(f"marks of student {i} in maths is:{m1}") 
#     print(f"marks of student {i} in english is:{m2}") 
#     print(f"marks of student {i} in sst is:{m3}") 

# f = open('filer', 'w' ) 
# lines = ["line1\nline2\nline3\n"] 
# f.writelines(lines) 
# f.close() 
#  # with open("emp", "r") as f: 
# #     print(type(f)) 


#     # f.seek(10) 
     
# #     print(f.tell()) 
# #     data = f.read(5) 
# #     print(data) 

# # with open('emp', 'w') as f:
# #     f.write('Hello world!') 
# #     f.truncate(5) 

# # with open('emp','r')as f:
# #     print(f.read()) 
    

def changecase(func): 
    def myinner(): 
        return func().upper() 
    return myinner 
@changecase 
def myfunction(): 
    return "Have a great day for you" 
print(myfunction.__name__) 

import functools 
def changecase(func): 
    @functools.warps(func) 
    def myinner(): 
        return func().upper() 
    return myinner 
@changecase 
def myfunction(): 
    return "Have a good day for you" 
print(myfunction.__name__) 


