# name = float(input('in(enter float input:'))
# print(f"this number is {name},{type(name)}")

#
# num1 = int(input("enter the number1: "))
# num2 = int(input("enter the number2: "))

# result1 = num1 * num2
# result2 = num1 / num2

# print(f"the multiply number is {result1}")
# print(f"the division number is {result2}")


# marital_status = input("Married (Y/N): ").lower()
# Age = int(input("Enter the age: "))
# Gender = input("Gender (M/F): ").lower()
#
# if Gender == 'f':
#     print("You will work only in Urban areas")
# elif Gender == 'm':
#     if 20 < Age < 40:
#         print("You can work in anywhere")
#     elif 40 < Age < 60:
#         print("You can work only in Urban areas")
#     else:
#         print("ERROR")


# principal = int(input("enter the principal: "))
# time = int(input("enter the time: "))
# rate = int(input("enter the rate: "))
# n = int(input("enter the N: "))

# S_I = (principal * time * rate)/100

# C_I = principal * (1+((rate/100)/n)) ** (n * time)

# print(f"The Simple Interest Amount is {S_I}")
# print(f"The Compound Interest Amount is {C_I}")

#
# side = int(input("enter the side: "))

# area = side * side
# perimeter = 4 * side

# print(f"the area of the square is: {area}")
# print(f"the perimeter of the square is: {perimeter}")

# a = 23
# # b = 23
# print(10 <= a <= 20)
# print(a >= 10 or a <= 20)
# print(not (10 <= a <= 20))

# continue statement
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         i = i + 1
#         continue;
#     print(i)
#     i += 1

# break statement
# i = 1
# while i <= 20:
#     if i == 7:
#         break
#     print(i)
#     i += 1

# num = 0
# while True:
#     num = int(input("Enter a positive number: "))
#     if num < 0:
#         break
#     else:
#         print("You entered:", num)

# sum = 0
# count = 0

# while count < 10:
#     num = int(input("Enter a number: "))
#     if num:
#         sum += num
#         count += 1

# print("The sum of the numbers is:", sum)

# for i in range(4,2, -1):
#     print(i)

# for i in range(4):
#     for j in range(2):
#         print(i,"*",j, "=", i * j)

# a = 122334
# print(str(a))

# num = int(input("enter the num: "))

# a = "mani"
# print(a[4:1:-1])

# a = "saravana"
# print(a[::-2])
# print(a,type(a))

#
# name = "saravana"
# for i in name:
#     print(i)

# name = input("enter value: ")
# for i in range(len(name)):
#     print(i,name[i])

# for i in range(2,21,2):
#     print(i)

# s = [2, 3, 4, 5, 4, 3, 2, 1, 4, 5, 6, 7, 8]
# new = []
# for i in s:
#     if (i not in new):
#         new.append(i)
#         s.sort()
# print(new)

# VASU SIR QUESTIONS
# 1. A store charges Rs.12 per item if you buy less than 10 items. If you buy between 10 and 99 items, 
# the cost is Rs.10 per item. If you buy 100 or more items, the cost is Rs.7 per item. 
# Write a program that asks the user how many items they are buying and prints the total cost
# item = int(input("enter the num of item: "))
# if item < 10:
#     t_cost = item * 12
# elif item <= 99:
#     t_cost = item * 10
# elif item >= 100:
#     t_cost = item * 7
# print(f"the total cost is {t_cost}")

# 2.Write a program that takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters. 
# For example, if the input is "HeLlO", it should return the list [0, 2, 4].
# str = input("enter a string: ")
# l = []
# for i in range(len(str)):
#     if i % 2 == 1:
#         l += str[i].lower()
#     else:
#         l += str[i].upper()
# print(l)

# 3. Write a program that prompts the user to input number of calls and 
# calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls
# calls = int(input("enter the num of calls: "))
# if calls <= 100:
#     bill = 200
# elif calls <= 150:
#     bill = 200 + (calls - 100) + 0.6
# elif calls <= 200:
#     bill = 200 + ()
