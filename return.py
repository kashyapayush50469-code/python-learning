'''num = int(input("Enter a number:")) 
temp = num 
digits = len(str(num))   
sum = 0 

for i in range(digits): 
    r = temp % 10 
    sum  += r ** digits 
    temp //= 10 
if sum == num: 
    print("Armsstrong number") 
else: 
    print("Not an Armsstrong number")
    
num = 2531

#arm_num = 153  = 1**3 + 5**3 + 3**3,  1+125+27 = 153

#arm_num= 
#  10 % 2 = 0
#  10 // 2 = 5

num = int(input("Enter a number:"))  # 25
temp = num  # 29 , 2 , 0
digits = len(str(num))    # 2
sum = 0 #, 81, 4, 85 

for i in range(digits):  # 0, 1
    r = temp % 10  # 29 % 10 = 9 , 2 % 10 = 2
    sum  += r ** digits  # 9**2 = 81 , 2 **2 = 4
    temp //= 10 

print(sum)
if sum == num: 
    print("Armsstrong number") 
else: 
    print("Not an Armsstrong number")




# This is for Calculating arms num
n = 153
str1 = str(n)  # "25" "2"
ln = len(str(n)) # 2 
srm_n = 0
for i in range(ln): #  0, 1 
    srm_n = srm_n + int(str1[i])**ln    # 0 + 2**2 = 4, 4 + 5**2 =  29

print(srm_n)
if srm_n == n:
    print("arms num")
else:
    print("not arms num")'''


# num = 121
# rev = 0 
# for i in num: 
#     rev = rev * 10 + num % 10 
#     num //= 10 
# print(rev)  
'''num = int(input("Enter an integer: "))

rev = 0
n = abs(num)   # handle negative numbers

# Count digits
count = 0
temp = n
while temp > 0:
    temp //= 10
    count += 1

# Reverse using for loop
for _ in range(count): 
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

# Restore sign if negative
if num < 0:
    rev = -rev

print("Reversed integer:", rev)'''

