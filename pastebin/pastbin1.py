fullname = input("Enter full name")
#Accept full name and display in reverse order with space between the words.

def rev(name):
    if not name.len:
        return ""
    print("reverse", name[::-1])


rev(fullname)