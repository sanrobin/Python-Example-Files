n = int(input("Enter the number: "))
s = 0
t = n
for i in range(1,n-1):
    if n % i == 0:
        s = s + i
if s == t:
    print(n,"is a perfect number.")
else:
    print(n,"is not a perfect number.")
    
