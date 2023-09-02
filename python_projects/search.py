# dicion = {"name": "saravana", "age": "23"}
import json
from difflib import get_close_matches

jsonfile = json.load(open("python_projects/data.json"))

word = input("enter the word: ")

def check(d):
    d = d.lower()
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys())) > 0:
        choice =  input("Did you mean %s, Enter Y for YES, N for NO: " %get_close_matches(d,jsonfile.keys())[0])
        if choice == "Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif choice == "N" or "n":
            return "This word is not exist, please give valid word!"
        else:
            return "It's a wrong choice, try again"    
    else:
        return "The word you mentioned doesn't exist, please enter the appropriate word!"
    
result = (check(word))

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)