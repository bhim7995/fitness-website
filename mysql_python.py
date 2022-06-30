import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root", database="studentss")
mycursor=mydb.cursor()
mycursor.execute("select * from Login")
# result=mycursor.fetchall()
result=mycursor.fetchone()
for i in result:
    print(i)