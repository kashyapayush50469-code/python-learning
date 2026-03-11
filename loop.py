"""Print numbers from 1 to 10 using a for loop.
Print all even numbers between 1 and 50 using a for loop.
Print all odd numbers between 1 and 20 using a for loop.
Write a program to find the sum of numbers from 1 to 100 using a for loop.
Write a program to calculate the factorial of a given number using a for loop.
Write a program to print the multiplication table of a given number using a for loop.
Write a program to count the number of characters in a string using a for loop.
Write a program to print each character of a string on a new line using a for loop.
Write a program to find the sum of all elements in a list using a for loop.
write a program to find the all elements in a list greater tahn 10 using for loop.""" 




'''# write first 10 netural numbers by using for loop.'''
for i in range(1, 11):
    print(i) 
'''# even numbers'''
for i in range(1, 51):
    if(i % 2 == 0):
        print(i) 
'''# odd numbers'''
for i in range(1, 20):
    if(i %2 != 0):
        print(i) 
'''# sum numbers.'''
total = 0 
for i in range(1, 101):
    total += i 
print("sum of numbers:", total) 

for i in range(16):
    print("15*", i, "=", 15*(i))
    if(i == 15):
        break 
       
'''# multiplication table using for loop.'''
a = 10 
for i in range(1, 101):
    print(a,"*", i, "=", i*a) 

for i in range(16):
    print("67*", i , "=", 67* (i)) 
    if(i == 15):
        break 

num = 5  
 
for i in range(1, 16):
    print(num, "*", i , "=", num*i) 
'''# prime numbes
# write the prime number for using for loop.
# for num in range(2, 21):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)'''

for i in range(2, 21):
    is_prime = True
    for x in range(2, i):
        if i % x == 0:
            if_prime = False
            break 
    if is_prime:
        print(i) 

'''# for num in range(2, 21):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num)

# Write a program to calculate the factorial of a given number using a for loop.'''
num = 3                  
fact = 1 

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)

'''# count the stinrg'''
text = "John" 
count = 0

for ch in text:
    count += 1

print("Number of characters:", count)


'''# Write a program to print each character of a string on a new line using a for loop.'''
a ="Hello"
for i in a:
    print(i) 

'''# Write a program to find the sum of all elements in a list using a for loop.'''
lst = [ 1, 5, 6, 78, 90, 45, 34]
total = 0 
for i  in lst:
    total += i 
print("sum of all numbers:", total) 

'''# write a program to find the all elements in a list greater tahn 10 using for loop.'''
lst1 = [1, 2, 3, 4, 5, 56, 78, 90, 45, 34, 23, 56, 55]

print("all numbers greater than 10:")
for x in lst1:
    if x > 10:
      print(x)  

'''#Q16. Write a program to calculate the sum of even numbers from 1 to 50 using a for loop.'''
sum_even = 0 
for  i in range(1,  20):
    if(i%2 == 0):
        sum_even+=i 
print("sum of even numbers:", sum_even)
'''# sum of odd numbers:'''
sum = 0 
for i in range(1, 40):
    if(i %2 != 0):
        sum += i 
print("sum of odd numbers", sum)  


'''# Q17. Write a program to print the ASCII value of characters in a string using a for loop.'''
text = "abcd" 
for ch in text:
    print(ch, "=", ord(ch))

'''# 18. Write a program to find the largest number in a list using a for loop.'''
list = [ 1, 2, 3, 34, 3, 5, 6, 67, 3, 4, 990] 
largest = list[0]
for i in list:
    if i > largest: 
      largest = i
print("largest numbers is:", largest)

'''# write a program to  check the largest value of the list using for loop.'''
lst = [1, 2, 3, 4, 5 ,56 ,6, 6 ,7, 345, 67, 562,34, 234,]
largest = list[0]
for i in list:
    if i >largest:
      largest = i
print("largest numgbers =", largest) 
'''# Q19. Write a program to count how many times a number appears in a list using a for loop.'''
l = [1, 2, 3, 4, 5, 4, 3, 4, 2, 4, 1, 4, 5]
count = 0 
search = 4 
for i in l:
    if i == search:
        count += 1 
print("Numbers", search, "apperas", count, "tmes") 

'''# Q20. Write a program to check whether a number is a palindrome or not using a for loop.'''
num = "678"
reverse_num = ""  

for i  in num:  
  reverse_num = i + reverse_num

if num == reverse_num:
    print("Palindrome number")
else:
    print("Not a palindrome number")

list4 = [2, 3, 4, 5]
product = 1
for i in list4:
    product *= i 
print(product)   
'''# average the following list'''
x = [1, 2, 3, 4, 6, 7]
total = 0 
for i in x: 
    total += i 
average = total /len(x)
print(average) 


'''# write program to the sting calculate the vowel for the following.'''
str = "Hello world"
vowels= "AEIOUaeiou"
count = 0 
for i in str:
    if i in vowels:
        count += 1 
print(count) 

'''#write program following this pattern using for loop. 1, 12, 123, 1234,''' 
rows = 5 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print() 

'''# Write a program to print the square of numbers from 1 to 10 using a for loop.'''

for i in range(1, 11):
    '''# print("Square of", i, "is", i * i)'''
    print(i*i)   

'''#Write a program to display the following pattern using a for loop: * ** *** ****'''
for i in range(1, 7):
    print("*" *i)  

'''# Print numbers in reverse order'''
for i in range(10, 0, -1):
    print(i)
'''# power of numbers.'''
base = 2
power = 3
result = 1
for i in range(power):
    result *= base
print(result)

'''# check prime numbers.'''
num = 7
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime") 
'''# reverse character in a string.''' 
s = "Python"
rev = ""
for ch in s:                                                                                                                                                                                 
    rev = ch + rev
print(rev)
'''# revese star string''' 
for i in range(4, 0, -1):
    print("*" * i)
'''# break pattern'''
for i in range(1, 10):
    if i == 5:
        break
    print(i)
'''# continue pattern'''
for i in range(1, 6):
    if i == 3:
        continue
    print(i) 
'''# nested loop''' 
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
'''# square pattern''' 
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

'''#while loop:- '''
'''# write numbers form 1 to 10 by using while loop.''' 
i = 1 
while i <= 10: 
    print(i) 
    i += 1  
'''# write numbers from 10 to 1 by using while loop.''' 
i = 10 
while i >= 1: 
    print(i)
    i -= 1  
'''# write even numbers form 1 to 20 by suing while loop.''' 
i = 2 
while i <=20: 
    print(i)
    i +=2 
'''# write even numbers form 1 to 50 bysuing while loop.''' 
i = 1 
while i <= 50:
    print(i)
    i += 2 
''' # table of number.''' 
x = 40 
i = 1 
while i <= 10: 
    print(x, "*", i, "=", x*i)
    i += 1  
'''# write 10 natural numbers by using while loop.'''
i = 1 
sum = 0 
while i <=50:
    sum += i 
    i += 1
print("sum = ", sum) 
'''# factiroal number''' 
n = 6 
fact = 1 
i = 1 
while i<= n: 
    fact *= i 
    i += 1  
print("factrioal", fact) 
'''# count digit in a number''' 
n = 453456
count = 0 
while n > 0: 
    count += 1 
    n //= 10 
print("Number of digits:", count) 
'''#reversre the number by using while loop.''' 
x = 3456 
rev = 0 
while x > 0: 
    rev = rev * 10 + x % 10
    x //= 10 
print("reverse=", rev)  
'''# check palindrome number: '''
n = 333
temp = n 
rev = 0 
while n > 0:
    rev = rev*10 + n % 10 
    n //= 10 
if temp == rev: 
    print("palindrome number")
else: 
    print("Not pailndrome") 
'''#sum of digit of a number '''
n = 4353453
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("Sum of digits =", sum) 
'''#Whiel square of numbers:''' 
i = 1 
while i <= 20:
    print( i * i)
    i += 1 
i = 1 
while i <= 30:
    print(i*i*i) 
    i += 1 
'''#character of a string'''
x = "Ayush"
i = 0 
while i < len(x):
    print(x[i])
    i += 1 
'''#count the character of the string by using while loop.''' 
x = "Ayush"
count = 0 
i = 0 
while i < len(x):
    count += 1 
    i += 1 
print("Total character:", count) 

'''# print pattern: '''
i = 1 
while i<= 4: 
    print("*" *i) 
    i += 1  
'''# write numbers divisable by 5(1 - 50)'''
i = 1 
while i <= 50:
    if i % 5 == 0: 
        print(i)
    i += 1 
'''#check weather a number is positive, negative or zero.''' 
n =  75
while True:
    if n > 0: 
        print("positive")
    elif n < 0: 
        print("negative")
    else:
        print("zero")
    break 
'''#write fibonacci serise:''' 
a = 0 
b = 1 
i = 1 
while i <= 10:
    print(a)
    c = a + b 
    a = b 
    b = c 
    i += 1 

'''Write a program to print the Fibonacci series up to n terms using a for loop.
Write a program to check whether a given number is an Armstrong number using a for loop.
Write a program to find the sum of all prime numbers between 1 and n using a for loop.
Write a program to reverse a number using a for loop.
Write a program to count the number of vowels and consonants in a string using a for loop.
Write a program to print the following number pattern using a for loop:
1, 12, 123, 1234, 12345
Write a program to find the largest and smallest number in a list using a for loop.
Write a program to check whether a given string is a palindrome using a for loop.
Write a program to calculate the power of a number (xⁿ) using a for loop without using built-in functions.
Write a program to find the frequency of each character in a string using a for loop.'''

n = int(input("Enter the of items:")) 
a, b = 0, 1  
for i in range(n): 
    print(a, end=" ") 
    a, b =b, a + b 

num = int(input("Enter a number:")) 
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
 
n = int(input("Enter the number:"))
sum = 0 
for num in range(2, n+1): 
    prime = True 
    for i in range(2, num): 
        if num % i ==0: 
            prime = False
    if prime: 
        sum += num 
print("sum of all numbers:", sum)

num = int(input("Enter the numbers:")) 
rev = 0 
for i in range(100000000):  
    rev = rev * 10 + num % 10 
    num //= 10 
    if num == 0: 
        break 
print("reversed number:", rev)


def myfunction(a):
        vowels = "aeiou" 
        consonant = "bcdfghjklmnpqrstvwxyz"
        vowels_count = 0
        consonant_count = 0
        for i in a: 
            for x in vowels:
                if i == x: 
                    vowels_count += 1
        for i in a: 
            for y in consonant: 
                if i == y: 
                    consonant_count += 1 
        print(vowels_count)
        print(consonant_count) 
myfunction("python is awesome" )
        

for i in range(1, 5): 
    for j in range(1, i + 1):
        print(j, end="") 
    print()

lst = [12, 45, 2, 19, 8]
largest = lst[0]
smallest = lst[0]

for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


s = input("Enter string: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")


x = int(input("Enter base: "))
n = int(input("Enter power: ")) 
result = 1

for i in range(n):
    result *= x

print("Result:", result)


s = input("Enter string: ")

for ch in s:
    count = 0
    for c in s:
        if c == ch:
            count += 1
    print(ch, ":", count) 


'''Armsstrong numbers in a range''' 
n = int(input("Enter the range:")) 
for num in range(1, n + 1): 
    temp = num 
    digits = 0 
    sum = 0 
    for _ in str(num): 
        digits += 1 
        temp = num 
        for _ in range(digits): 
            d = temp % 10 
            power = 1 
            for _ in range(digits): 
                power *= d 
            sum += power 
            temp //= 10 
    if sum == num: 
        print(num) 
'''nested  for loop'''
'''perfect Numbers in a list:''' 
lst = [1, 5, 3, 23, 12, 45] 
for num in lst: 
    sum_n = 0 
    for i in range(1, num): 
        if num % i ==0: 
            sum_n += i 
    if sum_n == num:
        print(num) 
'''armsstrong number in range''' 
n = int(input("Enter range:")) 
for num in range(1, n + 1): 
    temp = num 
    digits = 0 
    sum = 0 
    for _ in str(num): 
        digits += 1 
    temp = num 
    for _ in range(digits): 
        d = temp % 10 
        power = 1 
        for _ in range(digits): 
            power *= d 
        sum += power 
        temp //= 10 
    if sum == num: 
        print(num)
'''Frequncey of element'''
lst = [1, 2, 2, 3, 1, 4] 
visited = [] 
for i in range(len(lst)):  
    if lst[i] not in visited: 
        count = 0 
        for j in range(len(lst)): 
            if lst[i] == lst[j]: 
                count += 1 
        print(lst[i], ":", count)  
        visited.append(lst[i]) 
'''prime factorization''' 
n = int(input("Enter the number")) 
for i in range(2, n + 1): 
    while n % i == 0: 
        print(i) 
        n//= i
'''second largest numbers:''' 
lst = [10, 5, 20, 8] 
largest = lst[0] 
second = lst[0] 
for i  in lst: 
    if i > largest: 
        second = largest 
        largest = i 
    elif i > second and i != largest: 
        second = i 
print("second largest:", second) 
'''pascal's triangle''' 
n = int(input("Enter the rows:")) 
for i in range(n): 
    val = 1 
    for j in range(i + 1): 
        print(val, end="") 
        val = val * (i - j)// (j + 1)
    print() 
'''# remove dpllicates order in a list'''
lst5 = [1, 2, 3, 4, 2, 5, 2, 6] 
lst = [] 
for i in lst5: 
    if i not in lst:
        lst.append(i)  
print(lst) 

'''matrix multiplication''' 
A = [[1, 2], [3, 4]] 
b = [[5, 6], [7, 8]] 
result = [[0, 0], [0, 0]] 
for i in range(2): 
    for j in range(2): 
        for k in range(2): 
            result[i][j] += A[i][k] * b [k][j] 

print(result) 

'''palindrome number list''' 
lst = [1, 2, 3, 4, 1] 
p = True 
for i in range(len(lst)//2): 
    if lst[i] != lst[-i -1]: 
        p = False 
print("palindrome number" if p else "Not pallindrome number")
 
"longest word" 
str1 = "find the maximum word in the sentence" 
st = str1.split() 
count = 0 
index = 0 
for i in range(len(st)): 
    max_word = len(st[i]) 
    if max_word > count: 
        count = max_word
        index = i 
print(st[index]) 

"longest word" 
sentence = "find the maximum word in the sentence"

max_word = ""
current_word = ""

for ch in sentence:
    if ch != " ":              # build the word
        current_word += ch
    else:                      # word ended
        if len(current_word) > len(max_word):
            max_word = current_word
        current_word = ""

# Check last word (important!)
if len(current_word) > len(max_word):
    max_word = current_word

print("Maximum word:", max_word)

'''binary to decimal''' 
binary = "1011" 
decimal = 0 
power = 0 
for i in range(len(binary)-1, -1, -1): 
    decimal += int(binary[i]) * (2 **power) 
print(decimal) 
'''missing number''' 
lst1 = [1, 2, 4, 5] 
n = 5 
for i in range(1, n + 1): 
    if i not in lst1: 
        print(i) 

'''Anagram check''' 
s1 = "listen" 
s2 = "silent" 
flag = True 
for ch in s1: 
    if s1.count(ch) != s2.count(ch): 
        flag = False
print("Anagram" if flag else "Not anagram") 

'''Dimnd pattern''' 
n = 4 
for i in range(n): 
    print(" " *(n-i-1) + "*"*(2*i+1)) 
for i in range(n-2, -1, -1): 
    print(" "*(n-i-1) + "*"*(2*i+1)) 

'''Gcd using for loop''' 
a = 24 
b = 36 
gcd = 1 
for i in range(1, min(a, b) + 1): 
    if a % i == 0 and b % i ==0: 
        gcd = i 
print(gcd) 

'''sum of digit''' 
sum = 0 
for i in range(1, 11): 
    sum += i % 12
    i //= 12
print("sum of digit", sum) 

'''Transpose  of matrix''' 
mat = [[1, 2], [3, 4]] 
trans = [[0, 0], [0, 0]] 
for i in range(2): 
    for j in range(2): 
        trans[j][i] = mat[i][j] 
print(trans) 

"All substring" 
s = "abc" 
for i in range(len(s)): 
    for j in range(i + 1, len(s) + 1): 
        print(s[i:j]) 

'''passwrd validation''' 
pwd = "Pass@123" 
upper = lower = digit = special = 0 
for ch in pwd: 
    if 'A' <= ch <= 'Z': 
        upper = 1 
    elif 'a' <= ch <= 'z': 
        lower = 1 
    elif '0' <= ch <= '9': 
        digit = 1 
    else: 
        special = 1 
if upper and lower and digit and special: 
    print("Valid password") 
else: 
    print("Invalid password")  

