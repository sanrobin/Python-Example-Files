q = int(input("Enter an integer: "))
r = []
cnt = 0
while q >=1:
    if q % 2 == 0:
        x = 0
        r.append(x)
    else:
        x = 1
        r.append(x)
    q = q // 2
    cnt = cnt + 1
for i in range(cnt-1,-1,-1):
    print(r[i],end='')

