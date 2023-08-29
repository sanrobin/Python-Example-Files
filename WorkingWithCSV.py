import csv 
fh = open("Student.txt","w",newline="\r\n")
cwriter = csv.writer(fh)
cwriter.writerow(["Rollno", 'Name', "Marks"])
for i in range(10):
    rno = int(input("Enter rollno: "))
    stuname = input("Enter name: ")
    marks = int(input("Enter marks: "))
    cwriter.writerow([rno, stuname, marks])
fh.close()
