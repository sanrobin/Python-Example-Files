x = int(input("Enter the value of x: "))
y = int(input("Enter the limit: "))
s = 0
for i in range(0,y+1):
    fact = 1
    for k in range(1,i+1):
        fact = fact * k
    s = s + (-x**i)/fact(i)
print(s)

