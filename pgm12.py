#Write python program to add 'ing' at the end of the string.
#  If already ends with 'ing', then add ly
string = input("Enter a string: ")
if len(string) >= 3:
    if string.endswith('ing'):
        string += 'ly'
    else:
        string += 'ing'
print("Modified string:", string)
