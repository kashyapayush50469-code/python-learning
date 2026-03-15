'''class employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i +1
            return i

    def __str__(self):
        return f"The name of employee is {self.name} str"

    def __repr__(self):
        return f"employee('{self.name}')  repr" 
    
    def __call__(self):
         print("Hey I am good!") 
def welcome():
    print("Hey you are welcome my friend.")
main = "A good boy"
print(__name__)
if __name__ == "__main__" :
    welcome()''' 




'''num1 = int(input("user input1 :"))   # 10  # when we input any integer via input() it will consider "string" 
num2 = int(input("user input2 :"))
 # 20

cal = int(input("Enter the number for Calculator Add(1), sub(2), mul(3) : "))


# 1. adding 1
# 2. Sub 2
# 3. Multi 3
# 4. Devide 

if cal == 1:
    print("Adding num1 and num2 :", num1 + num2) 
elif cal == 2:
    print("Sub num1 and num2 :", num1 - num2)
elif cal == 3:
    print("mult num1 and num2 :", num1 * num2)
else :
    print("devide num1 and num2 : ", num1/num2) 




#       0, 1, 2, 3, 4
# print(lst[0]) 1
# print(lst[1]) 2
# print(lst[2])
# print(lst[3])
# print(lst[4])

# I want each data from this list.

#print(range(5))

# for num in [1,2,3,4,5]:   firt method
#     print(num)



# for num in lst:  secound method
#     print(num)

# lst = [5, 4, 3, 2, 1, 10, 40, 10,40,50,60,70,90]
# # x    0

# n = len(lst)
# print("len of lst : ", n)

# for x  in range(n): # 0,1,2,3,4
#     print(lst[x])   # print(lst[0])
#                     # print(lst[1])
#                     # print(lst[2])
#                     # print(lst[3])
#                     # print(lst[4])
   

#lst = [1,2,3,4]

# x = lst[0]
# y = lst[1]
# z = lst [2]
# a = lst[3]

# print(x + y + z + a)
lst = [1,2,3,4]
count = 0 # 1, 3, 6, 10

for x in range(len(lst)): # len = 4
    # x = 0, 1 ,2, 3
    count = count + lst[x] # lst[1] = 2, 
    #count = 1 + 2 = 3

answer - 24
# If condition
# elif condition
# else

# Equal - ==
# Not eqaul - !=
# Grater than- >
# Less than - <
# graater than equal- >=
# less than equal- <= 

# x = 6
# y = 5

# if x > y :
#     print("x is greater than y")
# elif x == y:
#     print("both are same")
# else:
#     print("y is greater than x")

x =5

if x>0:   
    print("yes this is greater")
    print("hello")

is_loged = True
is_loged = 6789

if is_loged:
    print("true")
else:
    print("false")


lst = [1,2,3,4]
count = 0 # 1, 3, 6, 10

for x in range(len(lst)): # len = 4
    # x = 0, 1 ,2, 3
    count = count + lst[x] # lst[1] = 2, 
print(count) 
    #count = 1 + 2 = 3 
# answer == 24'''
#leat code
'''class solution: 
    def __init__(self, nums):
     lst = []
     for i in range(len(nums)): 
        if i == 2: 
            break  
        lst.append(i) 
     print(lst) 
x = solution(nums=[1,7,11,15]) 
#longest substring without duplicates character.
class duplicatenumber:
    def __init__(self, x):
        lst1 = [] 
        count = 0
        for i in x:   
         if i not in lst1:
            lst1.append(i) 
            if lst1 == 1: 
                break 
            count += 1 
        print(count)  
a = duplicatenumber(x="bbbbbbbb")'''

# lst = [] 
# nums = [2, 7, 5, 4]
# count = 0
# for i in range(len(nums)): 

'''two sum numbers'''
def twosum():
    target = 9
    nums = [2, 7, 5, 4] 
    for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
print(twosum())

nums = [1,1,2] 
n = len(nums) 
i=j=1 
while i<n: 
      if nums[i] != nums[i-1]: 
            nums[j] = nums[i] 
            j+=1
      i+=1 
print(j) 

print(0) 
print(1) 
count = 2 
def fibonacci(prev1,prev2): 
      global count 
      if count <= 19: 
            newfibo = prev1 + prev2 
            print(newfibo) 
            prev2 = prev1
            prev1 = newfibo 
            count += 1 
            fibonacci(prev1,prev2) 
      else: 
            return 
fibonacci(1,0) 


