c = 1
for i in range(1,5):
	print("  "*(4-i),end = " ")
	while i>0:
		print(i,end = " ")
		i -= 1
	c += 1

	for x in range(2,c):
		print(x , end= " ")
	print()