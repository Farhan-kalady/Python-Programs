# Arrange characters in a string such that lowercase letters must come first

def lowercase(s):
    lower = ""
    upper = ""

    for ch in s:
        if ch.islower():
            lower += ch
        elif ch.isupper():
            upper += ch

    return lower + upper        

string = "pyThOn"
print(lowercase(string))                