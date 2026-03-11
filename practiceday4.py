"""Question: Write a program which will find all such numbers which are 
divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
def divisiable_by7(n, num):
        for i in range(n, num): 
            if i % 7 == 0 and i % 5 != 0:
                 print(i) 
divisiable_by7(2000, 3201)
'''2.Question: With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8 Then, the output 
should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''
def integral_number(n, m):
        dic = {}
        for i in range(n, m): 
            dic[i] = i * i 
        print(dic) 
integral_number(1, 9) 

'''3. the output will be HELLO WORLD, PRACTICE MAKES A MAIN PERFECT'''      
def upper_function(num): 
      print(num.upper()) 
upper_function(num="hello world.") 
upper_function(num="practice makes a main perfect.") 