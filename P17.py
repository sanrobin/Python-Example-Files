n = int(input("Enter a number: "))
l = len(str(n))
s = 0
t = n
while t != 0:
    s = s + ((t % 10) ** l)
    t = t // 10
if s == n:
    print(n,"is an armstrong number!")
else:
    print(n,"is not an armstrong number!")
    
