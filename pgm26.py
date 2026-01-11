# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String

def middle_of_string(s):
    if len(s) < 7 or len(s) % 2 == 0 :
        return "String length must be odd and greater than 7" 
    mid = len(s) // 2
    return s[mid -1 : mid +2]

string = input("Enter a string of odd length greater than 7: ")
print(middle_of_string(string))
