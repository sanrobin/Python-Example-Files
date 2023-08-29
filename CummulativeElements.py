list = [1,3,5,7,8]
finallist = [list[0]]
for i in range(1,len(list)):
    finallist += [finallist[i-1]+list[i]]
print(finallist)
