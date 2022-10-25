import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def definition(w):
    w=w.lower()
    title=w.title()
    W=w.upper()
    if w in data:
        return data[w]
    elif title in data:
        return data[title]
    elif W in data:
        return data[W]
    elif len(get_close_matches(w,data.keys(),cutoff=0.75))>0 :
        ans=input( "Did you mean {} . type 'Y' if you mean it or type 'N' for no : ".format(get_close_matches(w,data.keys(),cutoff=0.75)[0].upper()))
        if ans.lower()=='y':
            return definition(get_close_matches(w,data.keys(),cutoff=0.75)[0])
        else:
            return "The word doesn't exist"
    else:
        return "The word doesn't exist . Please verify it"


word = input("Enter the word: ")

output=definition(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)


