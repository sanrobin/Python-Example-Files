y = int(input("Enter the year in YYYY format: "))
j = y % 4
k = y % 400
l = y % 100
if (j == 0 or k == 0 or l == 0):
    print("It is a leap year")
else:
    print("It is not a leap year.")
