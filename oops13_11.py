# class Person:
#     name  = ''
#     age = 0
#
#     def __init__(self, nm, ag):
#         self.name = nm
#         self.age = ag
#
# ob1 = Person('Vishnu Prathap',24)
# ob2 = Person('Allen',23)
#
# print(ob1.name,ob1.age)
import math


# class Person:
#     name  = ''
#     age = 0
#
#     def __init__(self):
#         self.name = input('Enter the name: ')
#         self.age = int(input('Enter the age: '))
#
# ob1 = Person()
# # ob2 = Person('Allen',23)
#
# print(ob1.name,ob1.age)


# Create a class named EEmployee with attributes name, age, id, salary
# also define a method showdetails to the employee class

# class Employee:
#
#     def __init__(self):
#         self.name = input('Enter the name: ')
#         self.age = int(input('Enter the age : '))
#         self.id = int(input('Enter the id: '))
#         self.salary = int(input('Enter the salary: '))
#
#     def show_details(self):
#         print('\nEmployee id: ',self.id,'\nName of Employee: ',self.name,'\nAge : ',self.age,'\nSalary : ',self.salary)
#
# ob1 = Employee()
# ob1.show_details()


# Create a class named library with attribute title,author,price and define methods getauthor(), gettitle(), getprice(),
# setauthor(), settitle(), setprice()

class Library:
    def __init__(self):
        self.title = input('Enter the title of the book: ')
        self.author = input('Enter the name of author: ')
        self.price = input('Enter the price of the book: ')

    def get_author(self):
        print('Author name = ', self.author)

    def get_title(self):
        print('Title of the book = ', self.title)

    def get_price(self):
        print('Price of the book = ', self.price)

    def set_author(self):
        self.author = input('Change the name of the author : ')

    def set_title(self):
        self.title = input('Change the title: ')

    def set_price(self):
        self.price = int(input('Change the price: '))


ob1 = Library()
ob1.get_title()
ob1.get_author()
ob1.get_price()
ob1.set_title()
ob1.set_author()
ob1.set_price()
ob1.get_title()
ob1.get_author()
ob1.get_price()


# Create a calss named Circle with attribute radius and also define methods calculatearea() and calculateperi()

class Circle:
    def __init__(self):
        self.radius = int(input('Enter the radius of the circle: '))

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print('Area of the circle = ', area)

    def calculate_peri(self):
        peri = 2 * math.pi * self.radius
        print('Perimeter of the circle = ', peri)


ob = Circle()
ob.calculate_area()
ob.calculate_peri()
