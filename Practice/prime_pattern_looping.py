"""-50 to -30"""
# i = -50
# while i <= -30:
#     print(i)
#     i += 1
# print("-------+-------")

# """-10 to -2"""
# i = -10
# while i <= -2:
#     print(i)
#     i+=1
# print("-------+-------")

# """500 to -1"""
# i = 500
# while i >= -1:
#     print(i)
#     i-=1
# print("-------+-------")

""" 1 to 50 ===> EVEN (and) 51 to 100 ==> ODD""" 
# n = int(input("enter the number: "))
# if n >= 1 and n <= 50:
#     i = 1
#     while i <= 50:
#         if i % 2 == 0:
#             print(f"{i} is EVEN")
#         i+=1
# elif n >= 51 and n <= 100:
#     i = 51
#     while i <= 100:
#         if i % 2 == 1:
#             print("ODD number is",i)
#         i+=1
# else:
#     print("1 to 100")
# print("-------+-------")

"""1 to 50 multiply of 5"""
# i = 1
# while i <= 50:
#     if i % 5 ==0:
#         print(i)
#     i+=1
# print("-------+-------")

# """1 to 50 endswith 5"""
# i = 1
# while i <= 50:
#     if i % 5 ==0:
#         if i % 10 == 5:
#             print(i)
#     i+=1
# print("-------+-------")

"""Find the number of 5 endswtih 5 in multiple of 17 from 1 to 100"""
# i = 1
# while i <= 100:
#     if i % 17 == 0:
#         if i % 10 == 5:
#             print(i)
#     i+=1
# print("-------+-------")

"""prime in function WITH SQRT"""
# def is_prime(num):
#     if num <=1:
#         return False
#     rt = int(num**.5)
#     for i in range(2,rt+1):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("enter the number: "))
# if is_prime(number):
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not a prime")

"""prime in function WITHOUT SQRT"""
# def prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("enter the number: "))
# if prime(number):
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not a prime")

""" STAR patterns"""
# for i in range(1,6):
#     print(i * "* ")
# print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print()
# for i in range(5,0,-1):
#     print(i * "* ")
# print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# """NUMBER patterns"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()
# print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()
# print()
# for i in range(0,6):
#     for j in range(5-i):
#         print(i+1, end=" ")
#     print()
# for i in range(0,5):
#     for j in range(i+1):
#         print(5-j, end=" ")
#     print()
# print()
# 
# num = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()
# print()
# for i in range(1,6):
#     for j in range(5,i+5):
#         print(j,end=" ")
#     print()
# print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print((2*i)-1,end=" ")
#     print()
# print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print((2*j)-1,end=" ")
#     print()
# print()
# 
# for i in range(5,0,-1):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print()
# print()

# 
"""pattern in ALPHABET"""
# ascii = 65
# for i in range(1,6):
#     for j in range(1,i+1):
#         rs = chr(ascii)
#         print(rs,end=" ")
#     ascii += 1
#     print()
# print()
# ascii = 65
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         rs = chr(ascii)
#         print(rs,end=" ")
#     ascii += 1
#     print()
# print()

# for i in range(5,0,-1):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print() 

# for i in range(5,0,-1):
#    for j in range(5,5+i):
#       print(j,end=" ")
#    print()

""" TRIANGLE PATTERN """

# res = "python"
# x = 0
# for i in res:
#     x += 1
#     print(res[0:x])
# for i in res:
#     x = x - 1
#     print(res[0:x])

"""1."""
rows = int(input("enter the num: "))
k = 2 * rows - 2
for i in range(0,rows):
   for j in range(0,k):
      print(end=" ")
   k = k - 2
   for l in range(0,i+1):
      print(" * ",end=" ")
   print()

"""2."""
for i in range(0, 6):
    print(' ' * (6 - i) + '* ' * i)