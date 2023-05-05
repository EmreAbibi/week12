import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db")
cur = conn.cursor()

cmd = "CREATE TABLE employee (\
    EmpID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    EmpName VARCHAR(30) NOT NULL,\
    EmpGender VARCHAR(30), \
    EmpPhone VARCHAR(30), \
    EmpBdate VARCHAR(30))"

cur.execute(cmd)
conn.close()
