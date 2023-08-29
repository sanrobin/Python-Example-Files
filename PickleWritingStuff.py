import pickle
stu = {}
stufile = open("C:\\Users\\lab\\Desktop\\Stu.dat", 'ab')
ans = 'y'
while ans.capitalize() == 'Y':
    rno = int(input("Ener roll no.: "))
    name = input("Enter Name: ")
    marks = float(input("Enter marks: "))
    stu["Rollno"] = rno
    stu['Name'] = name
    stu["Marks"] = marks
    pickle.dump(stu,stufile)
    ans = input("Do you want to enter more records [Y/N]: ")
stufile.close()
print("Program Over!")