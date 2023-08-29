import mysql.connector as sqltor

def output():
    for i in data:
        print(i)

con = sqltor.connect(host = "localhost",user = "root",passwd = "",database = "student")
if con.is_connected():
    print("Successfully connected to the database!")
else:
    print("Error, Exiting...")
cur = con.cursor()
cur.execute("show tables")
data = cur.fetchall()
output()
cur.execute("select * from actor_info")
data = cur.fetchall()
output()
