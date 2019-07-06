#!C:\Users\PUJITH SAI KUMAR K\AppData\Local\Programs\Python\Python37-32\python.exe

import mysql.connector as conn

def htmlTop():
	print("""Content-type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>My server-side template</title>
				</head>
				<body>""")

def htmlTail():
	print("""</body>
			</html>""")

def execute(db_name,sql):
	db = conn.connect(host='localhost', user='root',passwd="",database=db_name)
	cursor = db.cursor()
	cursor.execute(sql)
	cursor.close()

if __name__ == "__main__":
	htmlTop()
	sql = "drop database studentdatabase"
	db_name = "studentdatabase"
	execute(db_name,sql)
	htmlTail()