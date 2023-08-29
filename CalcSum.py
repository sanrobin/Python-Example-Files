# Program CalcSum.py to add two numbers through a function.
def CalcSum(x,y):
    s = x + y                       # Statement 1
    return s                        # Statement 2

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
sum = CalcSum(num1, num2)
print("Sum of two given numbers:", sum)