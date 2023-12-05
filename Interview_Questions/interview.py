# 1 reverse a string in python
# str = input("enter the string: ")
# res = str[::-1]
# print(res)

# i = input("enter a string: ")
# res = i * 3
# print(res)

# s = "Hello World! 123$"
# print(s.upper())

# s = int("1235")
# print(s)

# indexing and slicing

# s = "Hello world!"
# print(s[1:9:2]) # output is "el o"
# print(s[::2]) # Hlowrd
# print(s[-4:-1:1]) # rld
# print(s[3::-1]) # lleH

# date ='12/02/1984'
# print(date[:5:-1][::-1])
# res = date.rsplit('/',1)
# print(res)

# x = input("enter the string1: ")
# y = input("ener the string2: ")
# print(x+y)

# s1 = "Hello"
# s2 = "polo"
# s3 = "Hello"
# print(s1 in s3) # True

# x = 99
# y = 100
# z = 200
# print("{1},{0},{2},{0}".format(x,y,z)) # 100,99,200,99

# print(bool()) # true
# print(bool('')) # false
# print(bool(None)) # true

# l = [1,2,3,4,5,6,7]
# print(l[:4:1])

# ITERATOR
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# An iterator is an object that contains a countable number of values.

# GENERATOR
# a generator is a function that returns an iterator that produces a sequence of values when iterated over. 
# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

# 
# for i in range(5, 0, -1):
#     for j in range(0, 5-i+1):
#         print(i, end=" ")
#     print()

# FINDING PRIME IN FOR LOOP 
# num = int(input("enter the num: "))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# PALINDROME
# num = (input("enter the num: "))
# # num1 = str(num) # to get a palindrome u need to change the integer into string
# if (num == num[::-1]):
#     print(f"the Number is Palindrome {num}")
# else:
#     print(f"ths Number is not a palindrome {num}")

# 
# s = ["Malayalam","hai"]
# s1 = s[0][::-1]
# print(s1)

# THIS ONE IS NOT AN INTERVIEW QUESTION 
# s = input("enter the string: ")
# res = ''
# for i in range(len(s)):
#     if i % 2 == 0:
#         res = s[i + 1] + res
#     else:
#         res = s[i - 1] + res
# res1 = res[::-1]
# print(res1)

# word = input("Enter an alphabet: ")
# vowels = "aeiouAEIOU"
# if word in vowels:
#     print("Vowel")
# else:
#     print("consonant")
print("-------------------------------")
# INTERVIEW QUESTIONS
# prime program

# import math
# num = int(input("enter the num: "))
# for i in range(2,int(math.sqrt(num))):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# 2 
# even = []
# odd = []
# for i in range(1,100):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# 
# def fibser(num):
#     if(num == 0):
#         return 0
#     elif(num == 1):
#         return 1
#     return fibser(num-1)+fibser(num -2)

# n = int(input("enter the num: "))
# for n in range(1,n+1):
#     print(n,end=" ")
# print("-------------")
# 
# def lpyr(n):
#     if n % 4 == 0 and n % 100 != 0:
#         if n % 400 == 0:
#             print(n,"is leap year")
#     elif n % 4 != 0:
#         print(n,"is not leap year")
#     return 
# leap = int(input("enter the year: "))
# res = lpyr(leap)
# print(res)

# import calendar
# print(calendar.isleap(2021))

# def func(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("enter the num: "))
# if func(number):
#     print("this is prime",number)
# else:
#     print("this is not prime number",number)

ls = [i for i in range(10) if i>5]
print(ls)
