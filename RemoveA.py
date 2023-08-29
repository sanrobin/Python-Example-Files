file1 = open("tkinter help.txt","r")
file2 = open("nswer.txt","w")
line = ""
string = ""
a = 0
lines = file1.readlines()
for line in lines:
    if 'a' not in line and 'A' not in line:
        file2.write(line)
        string += line
print("File modified is:")
print("------------------------------------")
print(string)
file1.close()
file2.close()