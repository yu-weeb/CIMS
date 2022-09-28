import mysql.connector as sql 
conn=sql.connect(host='localhost',user='host',passwd='admin',database='cims')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create table cand_details(AdhaarNumber int primary key, CandidateName varchar(50), DOB char(10),Email varchar(20),GuardianName varcar(15),Phone char(10),Course varchar(6))')
print ('Table created')
