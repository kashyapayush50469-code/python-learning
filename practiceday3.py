''' 3. Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''

'''num = int(input("Enter the number:"))  
for i in range(1, num + 1): 
    for j in range(1, i + 1):  
        print(i, end=" ") 
    print() '''

'''22. Print the Sum of a Current Number and a Previous number
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3''' 
def current_previous(num):

    for i in range(num): 
        if i == 0: 
            print(i, 0, 0)  
        else: 
            print(i, i - 1, i + (i - 1))  
current_previous(11) 
'''1. Check if the first and last numbers of a list are the same
        numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False'''

def first_last(num): 
    first = num[0] 
    second = num[-1] 
    if first == second: 
        return True
    else: 
        return False
num = [75, 65, 35, 75, 30]
print(first_last(num))  

a = "ayush" 
rev ="" 
for i in a: 
    rev = i + rev 
print("reversed string", rev) 


