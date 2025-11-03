# write a pgm to creates a single string seperated with space from strings by swapping the character at position 1.
# (b)create a list colours from comma separated list of colour names enterd by user.Print alternate colours.

s1=input("Enter a string: ")
s2=input("Enter another string: ")
swap1=s1[0]+s2[1]+s1[2:]
swap2=s2[0]+s1[1]+s2[2:]
print("After swapping: ",swap1+" "+swap2)

color=input("Enter colours separated by comma: ")
list=color.split(',')
print("Alternate colors:",list[::2])