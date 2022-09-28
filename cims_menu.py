                                                                                        #FUNCTIONS USED#
def choice1(v_aadharcard,v_candidatename,v_course):
    c1.execute("insert into cand_details(AadharNumber, CandidateName, DOB, Email, GuardianName, Phone, Course) values (%s, %s, %s, %s, %s, %s, %s)",
    (v_aadharcard, v_candidatename, v_dob, v_email, v_gname, v_phone, v_course))
    print(" ")
    print("                                        You are Enrolled Mr.",v_candidatename,". Congrats!!!")
    conn.commit()
    print(" ")
    print ("                                    Your enrollment for", v_course ,"course is successful!")
    return;

def enroll_deletion(change_adhaar_no):
    delpart= str(change_adhaar_no)
    c1.execute("delete from cand_details where AadharNumber = %s", (delpart,))
    print("")
    print("                                                  Successfully removed")
    conn.commit()
    return;


def name_edit(change_adhaar_no):
    change_name=str(input("Enter the desired name:") )
    delpart=str(change_adhaar_no)
    ahdaar=" where AadharNumber = ", (delpart,)
    c1.execute("update cand_details set CandidateName = %s", (change_name,), " where AadharNumber = ", (delpart,))
    print("")
    print("                                                  Successfully edited")
    conn.commit()
    return;

def course_edit(change_adhaar_no):
    change_course=input("Enter the Course: ")
    if change_course=='JAVA':
        change_course='JAVA'
    elif change_course=='Python':
        change_course='Python'
    elif change_course=='C#':
        change_course='C#'
    elif change_course=='BASIC':
        change_course='BASIC'
    elif change_course=='HTML':
        change_course='HTML'

    c1.execute("update cand_details set Course = %s", change_course, " where adhaar_no =%s ", str(change_adhaar_no))
    print("")
    print("                                               Successfully modified")
    conn.commit()









                                                                       #Front End#
import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='host',passwd='admin',database='cims')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
print("                                 Computer Institute Management System")
print(" ")
print("1. Enrolling For A Course")
print("2. Edit Enrollments (as admin)")
print("3. Display Details")
print("4. Exit")
choice=int(input("Enter the Choice - "))
if choice==1:
    v_aadharcard=input("Enter the Aadhar card Number: ")
    v_candidatename=input("Enter your name : ")
    v_year=int(input('Enter year of birth:'))
    v_month=int(input('Enter month of birth:'))
    v_day=int(input('Enter day of birth:'))
    v_dob=datetime.date(v_year,v_month,v_day)
    v_email=input('Enter email ID:')
    v_gname=input("Enter Guardian's name:")
    v_phone=int(input('Enter phone number:'))
    v_course=input("Enter the Course:")
    if v_course=='JAVA' or v_course=='Python' or v_course=='C#' or v_course=='BASIC' or v_course=='HTML':
       choice1(v_aadharcard,v_candidatename,v_course)
       
       c1.execute('select * from cand_details')
    else:
        print('Oops! No such course in system!')

    
    
if choice==2:
    uname=input("Enter Username:")
    passwd=input("Enter Password:")
    u_name='abc'
    pass_wd='123'
    if (uname==u_name) and (passwd==pass_wd):
        print("                                                      Password Accepted")
        print("1. Delete An Enrollment")
        print("2. Edit Name")
        print("3. Edit Course")
        print(" ")
        option=int(input("Which of the above options would you like to choose ?:"))

        if option==1:
            change_adhaar_no=int(input("Enter the Aadhar card no. of the candidate to be removed:"))
            enroll_deletion(change_adhaar_no)
            
        if option==2:
            change_adhaar_no=int(input("Enter the Aadhar number of the candidate whose name is to be changed:"))
            name_edit(change_adhaar_no)
            
        if option==3:
            change_adhaar_no=int(input("Enter the adhaar number of the candidate whose course is to be changed:"))
            course_edit(change_adhaar_no)
           
    else:
        print("                                         Wrong Username or Password")

    
if choice==3:
        c1.execute("Select * from cand_details ")
        data=c1.fetchall()
        for row in data:
            print("                                                            Candidates Details ")
            print("                                                      AdhaarNumber : ", row[0])
            print("                                                      CandidateName   : ", row[1])
            print("                                                      DOB : ", row[2]     )                                                 
            print("                                                      Email  : ", row[3])
            print("                                                      GuardianName : ", row[4])
            print("                                                      Phone : ", row[5])
            print("                                                      Course : ", row[6])
                  

if choice==4:
    print('                                                         Thank You!')
          




