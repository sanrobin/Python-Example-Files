num = int(input("Enter a 3-digit number: "))
f = num
sum = 0
while f > 0:
    a = f % 10
    f = int(f / 10)
    sum = sum + (a**3)
if sum == num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
