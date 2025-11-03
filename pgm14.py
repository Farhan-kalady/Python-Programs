#Generate a string by combining first two characters and last two characters from an input string. 
# If length of input string is 2, then resultant string must be a concatenation of those characters
#  or if length is less than 2, return an empty string instead.
input_string = input("Enter a string: ")
if len(input_string) >= 2:
    result = input_string[:2] + input_string[-2:]
else:
    result = ""
print(result)
