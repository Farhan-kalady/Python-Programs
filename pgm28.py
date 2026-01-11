""" Write a Python program to check the validity of password input by users.
Validation :
• At least 1 letter between [a-z] and 1 letter between [A-Z].
• At least 1 number between [0-9].
• At least 1 character from [$#@].
• Minimum length 6 characters.
• Maximum length 16 characters. 
"""

import re

password = input("Enter a Password")

if (len(password) < 6 and len(password) > 16):
    print("Inavlid password") 
elif not re.search("[a-z]", password):
    print("Inavlid password")
elif not re.search("[A-Z]", password):
    print("Inavlid password")
elif not re.search("[$#@]", password):
    print("Inavlid password") 
elif not re.search("[0-9]", password):
    print("Inavlid password")
else:
    print("Valid Passwword")           

        
