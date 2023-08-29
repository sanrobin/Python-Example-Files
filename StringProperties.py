str1 = input("Enter a string: ")
uppercount = lowercount = 0
alphacount = digitcount = 0
alnumcount = spacecount = 0
othercount = 0
for ch in str1:
    if ch.isalnum():
        alnumcount += 1
        if ch.isupper():
            uppercount += 1
        elif ch.islower():
            lowercount += 1
        elif ch.isalpha():
            alphacount += 1
    if ch.isdigit():
        digitcount += 1
    elif ch.isspace():
        spacecount += 1
    else:
        othercount += 1

print("Number of alphabets and digits:",alnumcount)
print("Number of capital alphabets:",uppercount)
print("Number of small alphabets:",lowercount)
print("Number of digits:",digitcount)
print("Number of spaces:",spacecount)
print("Number of other characters:",othercount)

