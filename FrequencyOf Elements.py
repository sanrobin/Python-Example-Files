# Frequency of an element in a list
l = [3,21,5,6,3,8,21,6]
l1 = []
l2 = []
for i in l:
    if i not in l2:
        x = l.count(i)
        l1.append(x)
        l2.append(i)
print("Element","\t\t\t","Frequency")
for i in range(len(l1)):
    print(l2[i],"\t\t\t",l1[i])
