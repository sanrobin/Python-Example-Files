try:
    x = float(input("Enter value of x: "))
    y = int(input("Enter the limit: "))
    s = 0
    for i in range(0,y+1):
        fact = 1
        for k in range(1,i + 1):
            fact = fatc * k
    print(s)
except NameError:
    print("Error")
