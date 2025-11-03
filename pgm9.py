#Numbers greater than 100 using list comprehension
nums = list(map(int, input("Enter numbers: ").split()))
new_list = [x for x in nums if x > 100]
print("Numbers greater than 100:", new_list)
