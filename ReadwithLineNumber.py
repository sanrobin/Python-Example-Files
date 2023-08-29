fh = open("tkinter help.txt","r")
l = fh.readlines()
count = len(l)
for i in range(count):
    print(str(i+1)+".", l[i],end = "")
fh.close()