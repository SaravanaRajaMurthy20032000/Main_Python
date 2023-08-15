""" 1. Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade."""
# students =[]
# for i in range(int(input("How many times?: "))):
#     name = input("Give the name: ")
#     score = float(input("His score?: "))
#     students.append([name,score])

#     second_lgr_score = sorted(list(set(score for name,score in students)))[1]
#     for name, score in sorted(students):
#         if score == second_lgr_score:
#             print(name)
"""2. Let's learn about list comprehensions! You are given three integers  and  representing
the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by 
on a 3D grid where the sum of  is not equal to .Here.
Please use list comprehensions rather than multiple loops, as a learning exercise."""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
res = [[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k != n]
print(res)
""" 3. Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up. """