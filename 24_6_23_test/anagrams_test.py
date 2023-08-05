"""1. Print lists of anagrams in the given list of words"""
list1 = ['cat','eat','madam','tac','tea','hai','act']
res = {}
for i in list1:
    new =''.join(sorted(i))
    if new not in res:
        res[new] = [i]
    else:
        res[new].append(i)
print(res.values())
for i in res.values():
    print(i)
