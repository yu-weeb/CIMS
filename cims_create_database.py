import mysql.connector as sql 
conn=sql.connect(host='localhost',user='host',passwd='admin')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create database cims')
print ('Database created')
