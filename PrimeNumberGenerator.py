x = int(input("Enter the limit for the generation of prime numbers: "))
for num in range(x + 1):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i = i + 1
    else:
        print(num,'is a prime number')
        
