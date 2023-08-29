L = [41,6,9,13,4,23]
m = max(L)
secmax = L[0]
for i in range(1,len(L)):
    if L[i] > secmax and L[i] < m:
        secmax = L[i]
print(secmax)
