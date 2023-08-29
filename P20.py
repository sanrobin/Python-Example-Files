n = int(input("Enter any number: "))
a = 0
t = n
while n > 0:
    r = n %10
    a = r + (a * 10)
    n = n // 10
if a == t:
    print("It is palindrome")
else:
    print("It is not palindrome")
