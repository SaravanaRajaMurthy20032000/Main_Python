"""items = [4,2,5,8,7,9,3]
for j in items:
    if j == 8:
        continue
    print(j)"""

def out_fun():
    msg1 = "Hai hello welcome to"
    def inner_fun():
        msg2 = " PythonGuru "
        res = msg1 + msg2
        return res
    return inner_fun

obj = out_fun()
print(obj())

""" MAP() """
def sqr(num):
    return num * num
    
res = [4,8,6,5,8,7,9]
print(set(map(sqr,res)))

""" Filter() """
def fun(i):
    if i <= 5:
        return i
        
res = filter(fun,(0,5,18,1,2.5,7,5,3,-1,-6))
print(list(res))