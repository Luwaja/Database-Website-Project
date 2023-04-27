import mysql.connector
from tabulate import tabulate

# open_database ==========================================================================
# Use: Opens database using host, user name, password, and database
def open_database(hostname, user_name, mysql_pw, database_name):
    global conn
    conn = mysql.connector.connect(host=hostname,
                                   user=user_name,
                                   password=mysql_pw,
                                   database=database_name
                                   )
    global cursor
    cursor = conn.cursor()

# printFormat ==========================================================================
# Use: Prints query results
def printFormat(result):
    header = []
    for cd in cursor.description:  # get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    return(tabulate(result, headers=header))  # print results in table format

# select and display query

# executeSelect ==========================================================================
# Use: Executes a select query and prints results
def executeSelect(query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res

# insert ==========================================================================
# Use: Inserts values into a table
def insert(table, values):
    query = "INSERT into " + table + " values (" + values + ")" + ';'
    cursor.execute(query)
    conn.commit()

# nextId ==========================================================================
# Use: 
def nextId(table):
    query = "select IFNULL(max(ID), 0) as max_id from " + table
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    return 1 if result is None else int(result) + 1

# executeUpdate ==========================================================================
# Use: Deletes a query and updates it
def executeUpdate(query):  # use this function for delete and update
    cursor.execute(query)
    conn.commit()

# close_db ==========================================================================
# Use: Closes the database
def close_db():  # use this function to close db
    cursor.close()
    conn.close()

##### Test #######
mysql_username = 'Luwaja'
mysql_password = 'MYfeeling23$'  
mysql_database = 'project'

open_database('localhost', mysql_username, mysql_password, mysql_database)  # open database

##### Test #######
'''mysql_username = 'MYMYSQLUSERNAME' # please change to your MySQL username
mysql_password ='MYMYSQLPASSWORD'  # please change to your MySQL password
open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   
executeSelect('SELECT * FROM ITEM'); # This is just a sample test, replace with your query
insert('ITEM',"22,'test',23.5,'M'")# This is just a sample test, replace with your query
executeSelect('SELECT * FROM ITEM where id = 22;')# checking if the value is updated
executeUpdate('delete from ITEM where id = 22;')# testing delete
executeSelect('SELECT * FROM ITEM where id = 22;')# checking if the id = 22 does not exist
executeUpdate("Update SUPPLIER set id = 20 where address ='Yemen';")# testing update
executeSelect("SELECT * FROM SUPPLIER where address = 'Yemen';")# checking the updated value
close_db()# close database'''
