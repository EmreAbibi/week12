import mysql.connector as sql

conn = sql.connect(host="localhost", user="root")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE USER 'flask'@'localhost' IDENTIFIED BY 'ubuntu';"
cur.execute(cmd)

cmd = "GRANT ALL PRIVILEGES ON *.* TO 'flask'@'localhost' WITH GRANT OPTION;"
cur.execute(cmd)

cmd = "FLUSH PRIVILEGES;"
cur.execute(cmd)

conn.close()
