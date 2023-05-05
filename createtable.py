import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE DATABASE flask_db"
cur.execute(cmd)
conn.close()
