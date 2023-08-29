def arCalc(x,y):
    return x+y, x-y, x*y, x/y, x%y

#__main__
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
add,sub,mul,div,mod = arCalc(num1, num2)
print("Sum of two given numbers:", add)
print("Subtraction of two given numbers:", sub)
print("Multiplication of two given numbers:", mul)
print("Division of two given numbers:", div)
print("Modulo of two given numbers:", mod)