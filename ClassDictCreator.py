classxi = dict()
n = int(input("Enter total number of section in XI Class: "))
i = 1
while i <= n:
    a = input("Enter section: ")
    b = input("Enter Stream name: ")
    classxi[a] = b
    i = i + 1
print("Class","\t","Section","\t","Stream Name")
for i in classxi:
    print("XI","\t",i,"\t",classxi[i])
