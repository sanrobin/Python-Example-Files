d1 = dict()
i = 1
n = int(input("Enter number of entries: "))
while i <= n:
    c = input("Enter the name of the country: ")
    cap = input("Enter the capital of the country: ")
    curr = input("Enter the currency of the country: ")
    d1[c] = (cap,curr)
    i = i + 1
l = d1.keys()
print("\nCountry\t\t\t","Capital \t\t","Currency")
for i in l:
    z = d1[i]
    print('\n',i,'\t\t',end="\t\t")
    for j in z:
        print(j,'\t\t',end="\t\t")
    # Searching
x = input("\nEnter Country to be searched: ")
for i in l:
    if i == x:
        print("\nCountry\t\t\t","Capital \t\t","Currency")
        z = d1[i]
        print('\n',i,'\t\t',end="\t\t")
        for j in z:
            print(j,'\t\t',end="\t\t")
        break
