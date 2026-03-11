'''Write a Python program to print all even numbers from 1 to 20.'''
'''num = int(input("Enter the number:"))
for i in range(1, num + 1):  
    if(i % 2 ==0): 
        print(i)'''  

def function(num): 
    for i in range(1, num + 1): 
     if i % 2 == 0:  
        print(i) 
function(50) 
'''Write a Python program to find the maximum element in a list.'''
def function(lst):
      lst.sort() 
      stg = lst[-1:] [0] 
      print(stg)
(function(lst= [1, 2, 3, 4, 50, 36, 23, 45]))  
       
'''Find the length of the longest word in a given sentence.'''
def longest_word(strs):
      stg = strs.split()
      index = 0 
      count = 0 
      for  i in range(len(stg)): 
         max_word = len(stg[i]) 
         if max_word > count: 
            count = max_word 
            index = i 
      print(stg[index]) 
longest_word(strs="find the lenght of the longestgaurav world in a given sentence")
'''#4 find the minimum word in the sentence:'''
'''5 find the word which is greater than equal to 5 need to raturn list''' 
'''6 find the word which is lesser than 5 '''
'''check the number of prime of prime number'''
'''Write a Python program to calculate the sum of digits in a number.'''
'''2. Write a Python program to find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]'''
'''Write a Python code to remove duplicates from a list'''
# strs = "Find the length of the longestgaurav word in aaaa given sentence."
# st =strs.split()
   

# index = 0
# count = 2
# for  i in range(len(st)): 
#      min_word = len(st[i])
#      if min_word <= count: 
#         count = min_word
#         index = i 
# print(st[index]) 
# print((function("Find the length of the longestgaurav word in a given sentence."))
# print((function("Find the length of the longestgaurav word in a given sentence."))
        
#         #         index = i 
# # print(stg[index])     

     
     

# sum = 0 
# for i in range(1, 11):  
#    sum += i % 12 
#    i //= 12 
# print("sum of numbers:", sum) 
# num = int(input("Enter the number:")) 
# for  i in range(2, num + 1):   
#    count = 0 
#    for x in range(1, i + 1): 
#       if i % x ==0: 
#          count += 1 
#    if count ==2: 
#       print(i) 