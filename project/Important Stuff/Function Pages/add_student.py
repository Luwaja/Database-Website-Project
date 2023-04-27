import sys
import python_db


#get the parameter; args[1] is the first parameter

name = sys.argv[1];  
major = sys.argv[2]; 

python_db.open_database('localhost', python_db.mysql_username, python_db.mysql_password, python_db.mysql_database)  # open database

#echo the name to the web page
values = "'{}', '{}', '{}'".format(python_db.nextId("STUDENTS"), name, major)
python_db.insert("STUDENTS", values)

python_db.close_db()

#print message to the web page
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Python - Add Student</title>")
print("</head>")
print("<body>")
print("<h2>Student Added Successfully</h2>")
print("<p>Name: " + name + "</p>")
print("<p>Major: " + major + "</p>")
print("</body>")
print("</html>")
