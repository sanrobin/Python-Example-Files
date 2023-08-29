f = 0
s = 1
a = int(input("enter the no of terms: "))
print(f , s , end = " ")
for i in range(0 , a):
    t = f + s
    f = s
    s = t
    print(t,end = ' ')
