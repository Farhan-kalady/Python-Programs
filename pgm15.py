#Accept percentage of marks from user and display the grade.
marks = float(input("Enter the percentage of marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'
print("Grade:", grade)
