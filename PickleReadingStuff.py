import pickle
with open("C:\\Users\\lab\\Desktop\\Stu.dat", "rb+") as fileout:
    stu = {}
    while True:
        stu = pickle.load(fileout)
        print(stu)