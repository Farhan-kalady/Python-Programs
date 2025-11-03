# Write a program to search an item in a given list and display the number of occurrences of the given item.
def search(item, term):
    count = 0
    for x in list(item):
        if x == term:
            count += 1

    return count


item = list(map(int,input("Enter the numbers").split(" ")))
term = int(input("Enter the Item to search"))
count = search(item, term)
if not count:
    print("Not found")
else:
    print("Count=",count)    
