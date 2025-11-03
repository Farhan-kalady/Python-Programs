#Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.

numberlist  = list(input("Enter the list").split(","))

def concat(li):
    print("Concatenated",end="")
    print("".join(map(str,li)))
    
concat(numberlist)