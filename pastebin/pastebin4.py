#Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list
numbers = list(map(int,input("Enter the numbers in comma separated form").split(",")))


def printeven(numbers):
    li=[]
    for x in numbers:
        if(x == 237):
            break
        
        elif(not x%2):
            li.append(x)
            
    return li
            
li = printeven(numbers)

print("Even are ",str(li))