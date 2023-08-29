n = 2
for i in range(2,50):
    j = 2
    while j <= i / 2:
        if i % j == 0:
            break
        j = j + 1
    if j > i / j:
        print(i,"is a prime number.")
print("Bye Bye!")
