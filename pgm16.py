#Evaluate using conditional statement(a) Check whether a given number is even or odd and return 'even' or 'odd' appropriately.
number = int(input("Enter a number: "))
print("Even" if number % 2 == 0 else "Odd")
#(b) Check whether an item is available in a list and return 'Available' or Not Available' appropriately.
items = input("Enter a list of items (separated by spaces): ").split()
item_to_check = input("Enter the item to check: ")
print("Available" if item_to_check in items else "Not Available")