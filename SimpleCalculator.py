def Sum():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x + y
    print("Solution is:",z)

def Multiply():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x * y
    print("Solution is:",z)

def Divide():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x / y
    print("Solution is:",z)

def Subtract():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x - y
    print("Solution is:",z)

def FloorDivide():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x // y
    print("Solution is:",z)

def Modulo():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = x % y
    print("Solution is:",z)

def Power():
    x = float(input("Enter the number: "))
    y = int(input("Enter power: "))
    z = x ** y
    print("Solution is:",z)

def SquareRoot():
    x = float(input("Enter the number: "))
    y = x ** 0.5
    print("Solution is:",y)

#__main__
while True:
    print("--------------------")
    print("     Calculator     ")
    print("--------------------")
    print("     1.Addition     ")
    print("    2.Subraction    ")
    print("  3.Multiplicatiion ")
    print("     4.Division     ")
    print("  5.Floor division  ")
    print(" 6.Modulus division ")
    print("       7.Power      ")
    print("   8.Square Root    ")
    print("        9.Exit      ")
    print("--------------------")
    choice = int(input("Enter your choice: "))
    print("--------------------")
    if choice == 1:
        Sum()
    elif choice == 2:
        Subtract()
    elif choice == 3:
        Multiply()
    elif choice == 4:
        Divide()
    elif choice == 5:
        FloorDivide()
    elif choice == 6:
        Modulo()
    elif choice == 7:
        Power()
    elif choice == 8:
        SquareRoot()
    elif choice == 9:
        print("Goodbye!")
        break
    else:
        print("Given option not valid.")