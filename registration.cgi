#!C:\Users\PUJITH SAI KUMAR K\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi

import mysql.connector as conn

import hashlib, binascii, os
 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def html_top():
    print("""Content-type:text/html\n\n
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8"/>
            </head>
            <body>""")

def html_tail():
    print("""    </body>
    </html>""")

def connectDB(db_name):
  db = conn.connect(host='localhost',user='root',passwd='',db=db_name)
  cursor = db.cursor()
  return db,cursor

def get_student_details(form_data):
    firstName = form_data.getvalue("firstName")
    lastName = form_data.getvalue("lastName")
    fatherFirstName = form_data.getvalue("fatherFirstName")
    fatherLastName = form_data.getvalue("fatherLastName")
    gender = form_data.getvalue("gender")
    DOB = form_data.getvalue("birthDate")
    address = form_data.getvalue("address")
    state = form_data.getvalue("state")
    city = form_data.getvalue("city")
    pincode = form_data.getvalue("pincode")
    emailID = form_data.getvalue("email")
    phoneno = form_data.getvalue("phoneno")
    password = hash_password(form_data.getvalue("password"))
    confirmPassword = hash_password(form_data.getvalue("confirmPassword"))
    student = [firstName, lastName, fatherFirstName, fatherLastName, gender, DOB, address, state, city, pincode, emailID, phoneno, password, confirmPassword]
    return student

def insertStudent(db,cursor,student):
  sql = "insert into student(firstName,lastName,fatherFirstName,fatherLastName,gender,DOB,address,state,city,pincode,emailID,phoneno,password) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9},'{10}','{11}','{12}')".format(student[0],student[1],student[2],student[3],student[4],student[5],student[6],student[7],student[8],student[9],student[10],student[11],student[12])
  cursor.execute(sql)
  cursor.close()
  db.commit()

#main program
if __name__ == "__main__":
    try:
        html_top()
        db_name = "studentDataBase"
        form_data = cgi.FieldStorage()
        db,cursor = connectDB(db_name)
        student = get_student_details(form_data)
        insertStudent(db,cursor,student)
        print("<h1> Data submission successful. </h1>")           
        html_tail()
    except:
        cgi.print_exception()
