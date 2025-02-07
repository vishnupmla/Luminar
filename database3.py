import sqlite3

con = sqlite3.connect("C:/Users/vishn/OneDrive/Documents/Luminar/Database/company.db")
if con:
    print('Successful')
else:
    print('Unsuccessful')


# k = con.execute('select sum(salary) from Employee')
# print(k.fetchall())
#
# k = con.execute('select max(salary) from Employee')
# print(k.fetchall())

# ALTER TABLE
#   add, drop, rename
# k = con.execute('UPDATE Employee SET salary=51000 WHERE empid = 1005')

# k = con.execute('ALTER TABLE Employee ADD place varchar(30) default "Not added"')
# con.commit()
# k =con.execute('ALTER TABLE Employee RENAME to employee')
# con.commit()

# RENAME COLUMN

# con.execute('ALTER TABLE Employee RENAME emp_id to id')
# con.commit()

'''  

To delete a table
DROP TABLE table_name

To create database file
CREATE DATABASE datatabse_file

To delete a DB file
DROP DATABASE database_name

'''