# Compare two lists entered by user?

def compare(list1, list2):
    if list1 == list2:
        return "List are same"
    elif sorted(list1) == sorted(list2):
        return "List have same elements"
    else:
        return "List are not equal"

list1 = [1, 2, 3]
list2 = [3, 2, 4, 1]

print(compare(list1, list2))