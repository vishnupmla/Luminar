import sqlite3

cn = sqlite3.connect("C:/Users/vishn/OneDrive/Documents/Luminar/Database/company.db")
if cn:
    print('Successful')
else:
    print('Unsuccessful')

# command = 'CREATE TABLE Employee(empid int PRIMARY KEY,name varchar(20),age int,phone int, salary int, gender varchar(6), deptid int)'
# cn.execute(command)

# insert = "INSERT INTO Employee VALUES(1003,'Allen',26,8156783421,33000,'male','dp102'),(1004,'Silpa',27,7623451055,50000,'Female','dp103')"
# cn.execute(insert)
# cn.commit()

# num_data = int(input('Enter the number of data to be added: '))
# for i in range(num_data):
#     emp_id = int(input('Enter the Employee ID : '))
#     name  = input('Enter the Name : ')
#     age = int(input('Enter the age : '))
#     phone = int(input('Enter the phone num : '))
#     salary = int(input('Enter the salary : '))
#     gender = input('Enter the gender : ')
#     dept_id = input('Enter the dept_id : ')
#
#     cn.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?,?)",(emp_id,name,age,phone,salary,gender,dept_id))
# cn.commit()

# k = cn.execute('SELECT * FROM Employee')
# print(k.fetchall())
#
# k = cn.execute('SELECT name,age,salary FROM Employee')
# print(k.fetchall())
#
# k = cn.execute('SELECT name, age, gender, salary FROM Employee WHERE salary > 45000')
# print(k.fetchall())

'''
Operators used in conditions
-------------------------------------
like - find pattern like structure in data
_ - Exactly one character
% - 0 or more character


between - to find within a range

'''

# k = cn.execute("select * from employee where name like 'A%'")
# print(k.fetchall())
#
# k = cn.execute("select * from employee where name like 'S____'")
# print(k.fetchall())
#
# k = cn.execute("select * from employee where name like 'K%a'")
# print(k.fetchall())

k = cn.execute("SELECT name,salary FROM Employee WHERE salary between 30000 and 48000")
print(k.fetchall())

k = cn.execute("SELECT name,salary FROM Employee WHERE salary in(28000,48000)")
print(k.fetchall())