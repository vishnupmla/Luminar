import sqlite3

con = sqlite3.connect("C:/Users/vishn/OneDrive/Documents/Luminar/Database/task.db")
if con:
    print('Successful')
else:
    print('Unsuccessful')

# con.execute("CREATE TABLE customer(customer_id int PRIMARY KEY, name varchar(30), place varchar(25))")
# con.execute("CREATE TABLE order_details(id int PRIMARY KEY, c_id int ,product varchar(20), price int, FOREIGN KEY(c_id) REFERENCES customer(customer_id))")

# con.execute("INSERT INTO customer VALUES(1,'Arun','Ekm'),(2,'Amal','Tvm'),(3,'Anu','Ekm'),(4,'Kiran','Tcr')")

# con.execute("INSERT INTO order_details VALUES(1,1,'laptop',37000),(2,4,'Mobile',25000)")

# con.execute("UPDATE order_details SET  product='Laptop' WHERE id=1 ")
# con.commit()

'''
Inner Join Syntax
--------------------------------
SELECT attribute FROM table1 INNER JOIN table2 on CONDITION

Reads all rows that have matching values in both tables
'''

# k = con.execute("SELECT * FROM customer INNER JOIN order_details ON customer.customer_id = order_details.c_id")
# print(k.fetchall())
#
# k = con.execute("SELECT name,id,product from customer JOIN order_details ON customer.customer_id = order_details.c_id where product='Laptop'")
# print(k.fetchall())

'''
Left Outer Join
------------------------
Returns all rows from left table and matching rows from right table. If no match null is returned for the columns 
from the right table.

Syntax:
select attribute from table1 left to table2 on condition

'''

# k = con.execute("SELECT * FROM customer LEFT JOIN order_details on customer.customer_id = order_details.c_id")
#
# k = con.execute("SELECT name,product,price FROM customer LEFT JOIN order_details on customer.customer_id = order_details.c_id where product='Laptop'")
# print(k.fetchall())

'''
Cartesian Join / Cross join
--------------------------------------
*returns cartesian product of rows from two tables(all combination of rows)
syntax
select attribute from table1 cross join table2
'''

# k = con.execute("SELECT name,id,product from customer cross join order_details")
# print(k.fetchall())


# -------------------------------------------------------------------------------------------------------------------------


# create two tables Books and Author
#
# Books  --bookno,title,author id(foreign),price,pages,published year
#
# Author ---author_id,name,nationality,birthyear
#
# 1,Find all books of specific author
# 2.Find the publication year of a particular book
# 3.Find the youngest author
# 4.List books with their corresponding author where booktitle contains a specific keyword
# 5.list all authors who have written books published after a particular year.

# con.execute("CREATE TABLE Books(book_no int PRIMARY KEY,title varchar(20),author_id int, price int, pages int, published_year int,FOREIGN KEY (author_id) REFERENCES Author(author_id) )")

# con.execute("CREATE TABLE Author(author_id int PRIMARY KEY, name varchar(30), nationality varchar(20), birth_year date)")

# con.execute("INSERT INTO Author VALUES(2,'Arthur Conan Doyle','British','1859-05-22'),(3,'J. K. Rowling','British','1965-07-31')")
# con.commit()

# con.execute("INSERT INTO Books VALUES(2,'Harry Potter',3,450,280,1997),(3,'Sherlock Holmes',2,400,230,1899),(4,'Eleven Minutes',1,250,130,2003),(5,'The Running Grave',3,300,250,2023)")
# con.commit()


# 1. Find all books of specific author
k = con.execute("SELECT name,title FROM Books INNER JOIN Author ON Books.author_id = Author.author_id where Author.name = 'Paulo Coelho'")
print(k.fetchall())


# 2.Find the publication year of a particular book
k = con.execute("SELECT * FROM Books WHERE title = 'The Alchemist'")
print(k.fetchall())

# 3.Find the youngest author
k = con.execute("SELECT name,max(birth_year) FROM Author")
print(k.fetchall())


# 4.List books with their corresponding author where booktitle contains a specific keyword
k = con.execute("SELECT title,name FROM Books INNER JOIN Author ON Books.author_id = Author.author_id WHERE Books.title LIKE('The%')")
print(k.fetchall())

# 5.list all authors who have written books published after a particular year.
k = con.execute("SELECT name,title,nationality,birth_year published_year FROM Books INNER JOIN Author on Books.author_id = Author.author_id WHERE published_year>2000")
print(k.fetchall())