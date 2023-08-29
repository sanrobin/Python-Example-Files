i = 1
s = 0
num = int(input("Enter the number: "))
while i < num:
    if num % i == 0:
        s += i
    i = i + 1
if s == num:
    print("It is a perfect number!")
else:
    print("It is not a perfect number.")
