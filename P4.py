a = int(input("Enter first no: "))
b = int(input("Enter second no: "))
c = int(input("Enter third no: "))
if a > b and a > c:
    print(a,"is greater")
elif a < b and b > c:
    print(b,"is greater")
else:
    print(c,"is greater")
