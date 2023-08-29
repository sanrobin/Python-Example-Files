import pickle
Names = ['First','Second','Third','Fourth','Fifth']
lst = []
for i in range(-1,-5,-1):
    lst.append(Names[i])
with open('Test.BAK','wb') as fout:
    pickle.dump(lst,fout)
with open('Test.BAK','rb') as fin:
    nlist = pickle.load(fin)
print(nlist)
