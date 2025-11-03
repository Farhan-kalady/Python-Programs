# Write a pgm to get a string from user (a) replace all occurences of first character with '$', except first character 
# (b) create a string from given string where first and last characters exchanged

s=input("Enter a string: ")
print("Original String : ",s)
s1=s[0]+s[1:].replace(s[0],'$')
print("Replaced string: ",s1)
l=len(s)
s2=s[l-1]+s[1:l-1]+s[0]
print("Exchanged string: ",s2)