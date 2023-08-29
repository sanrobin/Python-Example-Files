i = 1
n = int(input("The limit for the pattern is: "))
while i <= n:
    j = 1
    while j <= i:
        print(j,end=' ')
        j = j + 1
    print()
    i = i + 1
