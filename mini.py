""" 1. write a program to reverse an integer """
# num = input("enter the number: ")
# res = num[::-1]
# print(res)
# res1 = reversed(num)
# res1 = ''.join(res)
# print(res1)
# """now with function"""
# def num(rev):
#     return rev[::-1]
# number = input("enter the number: ")
# print(num(number))

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
def swap_num(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
res = swap_num(num1,num2)
print(res)
