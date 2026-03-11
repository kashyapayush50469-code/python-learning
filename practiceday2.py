'''#4 find the minimum word in the sentence:'''
'''5 find the word which is greater than equal to 5 need to raturn list''' 
'''6 find the word which is lesser than 5 '''
'''check the number of prime of prime number'''
'''Write a Python program to calculate the sum of digits in a number.'''
'''2. Write a Python program to find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]'''
'''Write a Python code to remove duplicates from a list'''


def greater_than5(strs):
    strs = strs.split(" ")
    lst =[]

    for word in strs:
            
            word_len = len(word)
            if word_len>= 5:
             print(word) 
greater_than5(strs = "Find the length of the longestGaurav word in a givenasdfghjksdfghjdfgh sentence.")


def shortest_word(strs):
        strs = strs.split(" ")
        lst =[]
        res = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for word in strs:
            word_len = len(word)
            ress = len(res)
            if word_len<ress:
             res = word
             lst.append(res) 
        print(lst) 
shortest_word(strs="Find the length of the longestGaurav word in a givenasdfghjksdfghjdfgh sentence.") 
    
def less_than(strs): 
    strs = strs.split(" ") 
    lst1 = [] 
    for i in strs: 
        x = len(i) 
        if x <= 5: 
            lst1.append(i) 
    print(lst1) 
less_than(strs="Find the length of the longestGaurav word in a givenasdfghjksdfghjdfgh sentence.")

num = [x for x in range(10)] 
print(num) 





