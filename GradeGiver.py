# A program to accept percentage of a student and display its appropriate grade.

perc = float(input("Enter the percentage of a student: "))

if perc > 85:
    print("Grade A")
elif perc > 70 and perc <= 85:
    print("Grade B")
elif perc > 60 and perc <= 70:
    print("Grade C")
elif perc > 45 and perc <= 60:
    print("Grade D")
else:
    print("Fail, Grade F")
