import mysql.connector as sqltor

def Connect():
    print("Trying to connect to server Please wait...")
    db = input("Please enter the name of the database: ")
    global connection
    connection = sqltor.connect(host = "localhost", user = "root", passwd = ".sanjay30", database = db)
    if connection.is_connected:
        print("Sucessfully connected to MySQL Server!")
    else:
        print("Error connecting to the server. Retrying...")
        Connect()

def Disconnect():
    print("Attempting to save changes and disconnect from server...")
    connection.commit()
    connection.close()
    if connection.is_connected == False:
        print("Sucessfully disconnected from MySQL Server!")

def Exit():
    print("Quitting...")
    quit()

#__main__
Connect()
cursor = connection.cursor()
print("Select one of the options below:")
print("1.Insert")
print("2.Disconnect")
a = int(input("Enter your option (1-2): "))
if a == 1:
    table = input("Enter the name of the table: ")
    z = True
    while z == True:
        col = input("Enter name of the column: ")
        print("Select the datatype of the value from below:")
        print("1.Integer")
        print("2.String")
        print("3.Float")
        dtype = int(input("Enter the type of data to be inserted(1-3): "))
        y = True
        while y == True:
            if dtype == 1:
                val = int(input("Enter the value for " + str(col) + ":"))
                y = False
            elif dtype == 2:
                val = input("Enter the value for " + str(col) + ":")
                y = False
            elif dtype == 3:
                val = float(input("Enter the value for " + str(col) + ":"))
                y = False
        query = "INSERT INTO {tablename}({column}) VALUES ({value})".format(tablename = table, column = col, value = val)
        cursor.execute(query)
        consent = input("Do you want to add more values(Y/N): ")
        if consent == "Y" or consent == "y":
            print("OK!")
        elif consent == "N" or consent == "n":
            print("OK! Exiting Insert mode...")
            z = False
        else:
            print("Invalid Choice!")
elif a == 2:
    Disconnect()
