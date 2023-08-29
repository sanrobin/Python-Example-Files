L = [33,13,92,99,3,12]
sum = 0
x = len(L)
for i in range(0,x):
    if type(L[i]) == int:
        if L[i] % 10 == 3:
            sum += L[i]

print(sum)
