l = [-12,11,-13,-5,6,-7,5,-3,-6]
n = len(l)
print("Original list:",l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j] < 0:
            l[j],l[j+1] = l[j+1],l[j]
print("After shifting list is:",l)
