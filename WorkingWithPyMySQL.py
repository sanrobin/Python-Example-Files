import pymysql
mycon = pymysql.connect(host = "localhost" ,user = "root" ,passwd = "prime", database = "g12")
cursor = mycon.cursor()
cursor.execute("select * from Physics")
data = cursor.fetchmany(3)
count = cursor.rowcount
for row in data:
    print(row)
mycon.close()