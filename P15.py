a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
while a != b:
    if a > b:
        a = a + b
    else:
        b = b - a
print("GCD is",a)
