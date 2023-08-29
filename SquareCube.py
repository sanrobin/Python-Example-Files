try:
    def main():
        while True:
            def Square(x):
                return x**2
            def Cube(x):
                return x**3
            print("Square or Cube\n")
            print("1.Square a number")
            print("2.Cube a number")
            print("3.Exit")
            ch = int(input("Enter your choice(1-3): "))
            if ch == 1:
                num = int(input("Enter the number to be squared: "))
                x = Square(num)
                print("The square of",num,'is',x)
            elif ch == 2:
                num = int(input("Enter the number to be cubed: "))
                x = Cube(num)
                print("The cube of",num,'is',x)
            elif ch == 3:
                print("Good Bye!")
                break
            else:
                print("Invalid Choice")
    main()
except TypeError or EOFError or ValueError:
    print("An Error occured! Resetting...")
    main()
