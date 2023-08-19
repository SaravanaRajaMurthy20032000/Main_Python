# # 1
# list = [('mango',12),('orange',20),('apple',34),('peach',55)]
# # print(list)

# lst1 = input("enter the string: ")
# lst2 = input("enter the num: ")
# lst_tuple = list(zip(lst1,lst2))
# print(lst_tuple)
# ##
# list = [('saravana'),('indhu'),('teja'),('harish')]
# l = []
# for i in list:
#     if i[0]:
#         l.append(i)
# print(l)

# words = ["Apple", "Orange", "Apple", "Banana", "Peach",  
#           "Banana", "Apple", "Peach", "Apple", "Banana","Apple"]
# count = {}
# for word in words:
#     if word not in count:
#         count[word] = 1
#     else:
#         count[word] += 1
# print(count)
# # print()
# print(count.items())


# word = ['apple','orange','peach','banana','apple','orange','banana','apple','peach','mango']
# c = {}
# for i in word:
#     if i not in c:
#         c[i] = 1
#     else:
#         c[i] += 1
# print(len(c.items()))
# print(sorted(c.items(), key=lambda x: x[1]))
# print(max(c.items(), key=lambda x: x[1]))
# print(min(c.items(), key=lambda x: x[1]))

def fun1(**kwargs):
    for i in kwargs.items():
        print(i)

def fun(*args):
    for i in args:
        print(i)

fun1(a=10,b=20,c=30)
fun(12,34,78,3)