# nobel_prize
#
# year   subject  winner   country category
#
# 1970 Physics  hannes  sweden  scientist
#
# ---
#
#
# 1).write a sql query to find the nobel prize winners for the year 1970(return year,subject and winner)
# SELECT winner,subject,year FROM nobel_prize WHERE year = 1970

# 2).write a sql query to find the nobel prize winnerin literature for 1971
# SELECT winner,subject,year FROM nobel_prize WHERE subject = literature and year =1971

# 3).sql to find the winners in the field of physics since 1978(return winner)
#SELECT winner FROM nobel_prize WHERE subject = 'Physics' and year >= 1978

# 4)sql query to find the winners in chemistry between 1970 and 1980
# SELECT winner FROM nobel_prize WHERE year between 1970 and 1980


# 5)sql query to find the details of the winners whose firstname match with string 'Louis'
#SELECT winner FROM nobel_prize WHERE name like 'Louis%'

# 6).sql query to find the winners excluding subjects physiology and Economics.
# SELECT winner FROM nobel_prize WHERE subject not in ('physiology','Economics')

import sqlite3


# con = sqlite3.connect("C:/Users/vishn/OneDrive/Documents/Luminar/Database/Task1.db")
con = sqlite3.connect("C:/Users/vishn/OneDrive/Documents/Luminar/Database/company.db")
if con:
    print('Successful')
else:
    print('Unsuccessful')

# command = "CREATE TABLE nobel_prize(id int PRIMARY KEY,year int,subject varchar(20),winner varchar(30),country varchar(20),category varchar(20))"
# con.execute(command)
# con.execute("INSERT INTO nobel_prize VALUES(102,1978,'Physics','Louis Philippe','Spain','Scientist'),(103,1979,'Literature','Glen Fest','Germany','Literature')")
# con.commit()

# k = con.execute('SELECT winner,subject,year FROM nobel_prize WHERE subject = literature and year =1971')
# print(k.fetchall())

k = con.execute('SELECT distinct(gender) FROM Employee')
print(k.fetchall())