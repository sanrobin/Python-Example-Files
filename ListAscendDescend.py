# Get n numbers and sort them in ascending and descending order

#__main__
ListN = []

n = int(input("Enter the total number of elements to be used: "))

for i in range(n):
    x = int(input("Enter the number for the list at index "+str(i)+": "))
    ListN.append(x)

ListN.sort()

print("The given numbers ins ascending order:")
for i in range(n):
    print(ListN[i], end = "\t")
print("\n")

ListN.reverse()

print("The given numbers ins descending order:")
for i in range(n):
    print(ListN[i], end = "\t")
