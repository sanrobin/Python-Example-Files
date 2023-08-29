a = int(input("enter a: "))
b = int(input("enter b: "))
ta = a
tb = b
while a != b:
    if a < b:
        a = ta + a
    else:
        b = tb + b
print("LCM is",a)
