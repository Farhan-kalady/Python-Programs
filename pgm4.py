#check the length of two sets are same or not.
#Check whether the sum of items in two sets are same or not.
#Check whether any item is present in both sets.
a=set(map(int,input("Enter first set of numbers : ").split()))
b=set(map(int,input("Enter second set of numbers : ").split()))
print("Is the lists are of same length: ",len(a)==len(b))

print("Is the lists sums to same value: ",sum(a)==sum(b))

print("Whether any value occur in both:",bool(a & b))