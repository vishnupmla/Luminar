import mysql.connector
#
# con = mysql.connector.connect(user='root',password='root',host='localhost',database='company')
# c = con.cursor() # Cursor object for executing sql commands
# #
# c.execute('CREATE TABLE employee(empid int PRIMARY KEY,name varchar(20),age int, gender varchar(20), place varchar(20),salary int)')
# print('Table created')

# c.execute('INSERT INTO employee VALUES(103,"Hari",21,"Male","Pathanamthitta",45000),(104,"Adithyan",25,"Male","Kottayam",41000),(105,"Punnoose",26,"Male","Kottayam",38000)')
# con.commit()
# print("Inserted")

# c.execute("select * from employee")
# k=c.fetchall()
# print(k)
# con.close()


# Books  --bookno,title,author id(foreign),price,pages,published year
#
# Author ---author_id,name,nationality,birthyear
#
# 1,Find all books of specific author
# 2.Find the publication year of a particular book
# 3.Find the youngest author
# 4.List books with their corresponding author where booktitle contains a specific keyword
# 5.list all authors who have written books published after a particular year.

con = mysql.connector.connect(user = 'root',password = 'root',host='localhost',database='mydb')
c = con.cursor()
# c.execute("CREATE DATABASE ")

# c.execute("CREATE TABLE Author(author_id int PRIMARY KEY, name varchar(30), nationality varchar(20), birth_year date)")
# c.execute("CREATE TABLE Books(book_no int PRIMARY KEY,title varchar(20),author_id int, price int, pages int, published_year date,FOREIGN KEY (author_id) REFERENCES Author(author_id))")
# print('Table created')

# c.execute("INSERT INTO Author VALUES(1,'Paulo Coehlo','Brazil','1947-08-24'),(2,'Arthur Conan Doyle','British','1859-05-22'),(3,'J. K. Rowling','British','1965-07-31')")

# c.execute("INSERT INTO Books VALUES(1,'The Alchemist',1,230,160,'1988-03-24'),(2,'Harry Potter',3,450,280,'1997-07-12'),(3,'Sherlock Holmes',2,400,230,'1899-09-28'),(4,'Eleven Minutes',1,250,130,'2003-04-16'),(5,'The Running Grave',3,300,250,'2023-12-1')")
# con.commit()

# 1.
# c.execute("SELECT name,title FROM Books INNER JOIN Author ON Books.author_id = Author.author_id where Author.name = 'Paulo Coehlo'")
# k= c.fetchall()
# print(k)
#
# # 2.
# c.execute("SELECT * FROM Books WHERE title = 'The Alchemist'")
# k= c.fetchall()
# print(k)

# # 3.
c.execute("SELECT name,birth_year FROM Author ORDER BY birth_year DESC limit 1 ")
k= c.fetchall()
print(k)

# # 4.
# c.execute("SELECT title,name FROM Books INNER JOIN Author ON Books.author_id = Author.author_id WHERE Books.title LIKE('The%')")
# k= c.fetchall()
# print(k)

# 5.
c.execute("SELECT name,title,nationality,birth_year published_year FROM Books INNER JOIN Author on Books.author_id = Author.author_id WHERE published_year>2000")
k= c.fetchall()
print(k)
con.close()
