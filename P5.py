a = int(input("Enter first subject marks(0-100): "))
b = int(input("Enter second subject marks(0-100): "))
c = int(input("Enter third subject marks(0-100): "))
d = int(input("Enter fourth subject marks(0-100): "))
e = int(input("Enter fifth subject marks(0-100): "))
s = a + b + c + d + e
t = s / 5
if t >= 90:
    g = 'A'
elif t < 90 and t >= 60:
    g = "B"
elif t < 60 and t >= 45:
    g = "C"
elif t < 45 and t >= 33:
    g = "D"
else:
    g = "E"
print("The total marks are {} out of 500".format(s))
print("The percentage is {}".format(t))
print("The grade is {}".format(g))
