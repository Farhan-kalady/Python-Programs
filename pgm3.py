#Check colors in list1 not in list2
#Remove duplicates from a list
#Check whether a list is empty or not
l1=set(list(input("Enter one list of color: ").split(',')))
print("List of color: ",l1)

l2=set(list(input("Enter another list of color: ").split(',')))
print("List of color: ",l2)

print("Colors in list1 not in list2:", l1 - l2)

l3=map(int,input("Enter numbers : ").split())
print("after removing duplicates: ",set(l3))

l4=list(input("enter numbers:").split())
print("List of numbers: ",l4)
print("List empty ",bool(not len(l4)))

