""" 1. write a program to reverse an integer """
# num = input("enter the number: ")
# res = num[::-1]
# print(res)

# res1 = reversed(num)
# res1 = ''.join(res1)
# print(res1)

# """now with function"""
# def num(rev):
#     return rev[::-1]
# number = input("enter the number: ")
# print(num(number))

# def rever(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str

# res = input("enter the value: ")
# print(rever(res))

""" 2. Write a program in Python to check given number is prime or not. """
# def is_prime(num):
#     if num <= 1:
#         return False
#     rt = int(num ** .5)
#     for i in range(2,rt+1):
#         if num % i == 0:
#             return False
#     return True
    
# number = int(input("enter the num: "))
# if is_prime(number):
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not a prime")
""" 3. Write a program in Python to print the Fibonacci series using function method. """
# n = int(input("please give a number for fibonacci series : "))
# first,second=0,1
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)

# for i in range(0,n):
#     print(f"fibonnaci series are {fibonacci(i)}")
""" 4. Write a program in Python to check whether a number is palindrome or not using iterative method. """
# def is_palindrome(number):
#     return number == number[::-1]

# num = input("Enter a number: ")
# if is_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")
""" 5. Write a program in Python to find greatest among three integers. """
# num1 = input("enter the person1: ")
# num2 = input("enter the person2: ")
# num3 = input("enter the person3: ")

# if (num1 > num2) and (num1 > num3):
#     print(f"{num1} is greatest")
# elif (num2 > num1) and (num2 > num3):
#     print(f"{num2} is greatest")
# else:
#     print(f"{num3} is the greatest")
""" 6. Write a program in Python to swap two numbers without using third variable? """
# def swap_num(a,b):
#     a = a+b
#     b = a-b
#     a = a-b
#     return a,b

# num1 = int(input("enter the num1: "))
# num2 = int(input("enter the num2: "))
# res = swap_num(num1,num2)
# print(res)
""" 7. Write a program in Python to find given number is perfect or not? """
# num = int(input("enter the number: "))
# res = []
# for i in range(1,num):
#     if num % i == 0:
#         res.append(i)

# if sum(res) == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")
""" 8. Write a method in Python which will remove any given character from a String. """
# def rm_str(sent,chrt):
#     res = sent.replace(chrt,"")
#     return res

# sent = input("enter the string: ")
# chrt = input("enter ther chr to change: ")
# print(rm_str(sent, chrt))
""" 9. Write a program in Python to count occurrence of a given character in a String? """
# def cnt(sent,chr):
#     count = 0
#     for i in sent:
#         if i == chr:
#             count += 1
#     return(count)

# sent = input("enter the string: ")
# chr = input("enter the chr to count: ")
# print(cnt(sent,chr))
""" 10. Write a program in Python to check if two String are Anagram. """
# def anagram(sent,chr):
#     if sorted(sent) == sorted(chr):
#         return True
#     else:
#         return False

# sent = input("enter the anagram: ")
# chr = input("enter the check str: ")
# print(anagram(sent,chr))
""" 11. Write a program in Python for, How to compare two array is equal in size or not. """
# def arr(ar1,ar2):
#     if len(ar1) == len(ar2):
#         return True
#     return False

# ar1 = input("enter the number: ")
# ar2 = input("enter the number2: ")
# print(arr(ar1,ar2))
""" 12. Write a program in Python to find largest and smallest number in array. """
# def sml_lgt(lgr,sml):
#     if lgr > sml:
#         return True
#     if sml > lgr:
#         return True
#     else:
#         return False

# lgr = input("enter the lagest num: ")
# sml = input("enter the smallest num2: ")
# print(sml_lgt(lgr,sml))
""" 13.Merge two sorted Arrays/Lists """
# def merge_two_list(one,one_2):
#     res = one + one_2
#     result = sorted(res)
#     return result

# num1 = [1,5,2,4]
# num2 = [9,7,8,0]
# print(merge_two_list(num1,num2))
""" 14.given an array of integers from 1 to n, with one number missing, 
write a function to find the missing number. for example, if the input array is [1,2,3,5], 
the function should return 3 in python """
# def find_missing_number(nums):
#     n = len(nums) + 1  # n is the expected length of the array
#     expected_sum = (n * (n + 1)) // 2
#     actual_sum = sum(nums)
#     missing_number = expected_sum - actual_sum
#     return missing_number

# input_array = [1, 2, 3, 5]
# missing_number = find_missing_number(input_array)
# print("Missing number:", missing_number)

# def miss_num(nums):
#     nums.sort()
#     for i in range(nums[0],nums[-1]+1):
#         if i not in nums:
#             return i 
        
# number = [1,2,4,7,3,9]
# print(miss_num(number))

# s = lambda x: x.sort()
# n = [3,5,1,2]
# s(n)
# print(n)

""" 15. Multiply two integers without using multiplication operator. """
# num1 = int(input("Enter a number for num1: "))
# num2 = int(input("Enter a number for num2: "))
# product = 0
# for i in range(1,num2+1):
#     product = product + num1
# print("Multiplication of numbers:",product)

"""16. How can you replace string space with a given character in Python?"""
# this is saravana answer
# def str_replace(sent):
#     rs = sent.replace(' ','o')
#     return rs

# res = input("enter the content: ")
# print(str_replace(res))
# # this is website answer 
# def str_replace(text,ch):
#     result = ''
#     for i in text: 
#             if i == ' ': 
#                 i = ch  
#             result += i 
#     return result

# text = "D t C mpBl ckFrid yS le"
# ch = "a"
# print(str_replace(text,ch))
# 'DataCampBlackFridaySale'

"""17. Given a positive integer num, write a function that returns True if num is a perfect square else False."""
# def ret_prft(num):
#     squr = int(num**.5)
#     check = squr**2 == num
#     return check

# print(ret_prft(10),ret_prft(36))

"""18. Find the missing number in the array""" # This is Amazon interview question
# def miss_num(list_num):
#     sum_numbers = sum(list_num)
#     n = len(list_num) + 1
#     op_numbers = (n * (n+1))/ 2
#     return int(op_numbers - sum_numbers)

# num = [1,7,3,2,5,6]
# print(miss_num(num))

"""19. We can write conditional expressions in a single line instead of writing using multiple
lines of if-else statements. It allows you to write clean and compact code.""" # #this is called ternary operator
# score = 70
# print('Fail' if score < 50 else 'Merit' if score <= 70 else 'Distinction') 

"""20. Summation of all numbers from 1 to 101"""
# print(sum(range(1,101)))

"""21. Is it possible to construct a Python program that calculates the mean of numbers in a list?"""
# n = int(input("enter the no.of.elements: "))
# l = []
# for i in range(1,n+1):
#     element = int(input("enter the number: "))
#     l.append(element)
# average_num = sum(l)/2
# print(round(average_num))
"""CRUD program in python without MYSQL"""
# CREATE
# file = open('example.txt', 'w')
# file.write('this is just an example line')
# file.close()
# # READ
# file1 = open('example.txt', 'r')
# res = file1.read()
# print(res)
# file1.close()
# UPDATE
"""FOR UPDATE SAME WRITE IS USED"""
# DELETE
# import os
# os.remove('example.txt')
""" Common words"""
# str_1 = "hai hello how are you"
# str_2 = "hello im fine, how about you"

# res_1 = set(str_1.split())
# res_2 = set(str_2.split())
# result = res_1 & res_2
# print(result)