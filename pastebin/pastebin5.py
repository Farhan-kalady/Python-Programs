characters  = input("Enter the string")

def removeod(characters):
    return characters[::2]

print("Even indexed", removeod(characters))

