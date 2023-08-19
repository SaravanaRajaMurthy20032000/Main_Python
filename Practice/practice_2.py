# age = int(input("enter age: "))

# if (50 < age < 60):
#     if (age % 2 == 0):
#         print(f"{age} is even and its 1st block")
#     else:
#         print(f"{age} is odd and its 1st block")
# elif (40 < age < 50):
#     if (age % 2 == 0):
#         print(f"{age} is even and its 2nd block")
#     else:
#         print(f"{age} is odd and its 2nd block")
# elif(60 < age < 70):
#     if (age % 2 == 0):
#         print(f"{age} is even and its 3rd block")
#     else:
#         print(f"{age} is odd and its 3rd block")
# else:
#     print(f"This is below and above the given age {age} and its in else block")

#
# for num in range(-2,-5,-1):
#     print(num, end=" ")

# a = int(input("enter the num: "))
# b = float(input("enter the num: "))
# c = a + b
# print(c)
# print(type(a))
# print(type(b))

#
# str1 = "Python "
# str2 = "Programming"
# str1 += str2
# print(str1)

# n = int(input("enter the num: "))

# if n >= 1 and n <= 50:
#     i = 1
#     while i <= 50:
#         if i % 2 == 0:
#             print(f"the {i} is even")
#         i += 1
# elif n >= 51 and n <= 100:
#     i = 51
#     while i <= 100:
#         if i % 2 != 0:
#             print(f" the {i} is odd")
#         i += 1
# else:
#     print("1 to 100")

#
# num = int(input("Enter a number: "))

# if num%2 == 0:
#     print(num**2)
# else:
#     if num % 5 == 0:
#         print(num**3)
#     else:
#         print(num*10)
# print("the fin")


# test
# a = 2
# a = 4
# a = 6
# print(a + a + a)

# print(1, 2, 3, 4, sep='#', end='&')

# str = ("""Hey""")
# print(len(str))

# str = 'it\'s ok'
# print(len(str))

# str = '\n'
# print(len(str))

# x = 11
# y = 4
# x = x % y
# x = x % y
# y = y % x
# print(x, y)

# a = 5
# b = 1
# c = a > b or b < a and a == 1
# print(c)

# answer_a = int(input('Try to guess the first number: '))
# if answer_a == 8:
#     answer_b = int(input('Correct! Now, guess the second number: '))
#     if answer_b == 5:
#         print('You won!')
#     else:
#         print('You only got one number right. So close!')
# else:
#     print('Wrong!')

# ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(ALPHABET[7:9])
# print(ALPHABET[-3:-1])
# print(ALPHABET[:3])
# print(ALPHABET[-1:])
# print(ALPHABET[14:-12])
# print(ALPHABET[1:-1])
# print(ALPHABET[0:5:2])
# print(ALPHABET[::-1])
# print(ALPHABET[5:2:-1])
# print(ALPHABET[14:10:-2])

# a = "1"
# b = 2
# print(int(a) + b)

# 4th QUESTION
# s1 = ''
# s2 = ' '
# print(bool(s1)) # Output: False
# print(bool(s2)) # Output: True

# string = input("enter the name to Split/Join: ")
# res = string.split()
# res1 = ''.join(string)
# print(res)
# print(res1)

# asc = 65
# for i in range(1,6):
#     for j in range(1,i+1):
#         res = chr(asc)
#         print(res,end=" ")
#     asc+=1
#     print()

"""RECURSION"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(7))