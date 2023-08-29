str1 = input("Enter a string: ")

print("Original string is :",str1)
str2 = ""
x = str1.split()
for a in x:
    str2 += a.capitalize() + " "
print(str2)

