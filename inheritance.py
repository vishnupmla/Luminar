# class A:
#     def meth1(self):
#         print('Function meth1 from class A')
#
#     def meth2(self):
#         print('Function meth2 from class A')
#
#
# class B(A):
#     def meth3(self):
#         print('Function meth3 rom class B')
#
#
# ob1 = A()
# ob2 = B()
#
# ob1.meth1()
# ob2.meth1()


class Person:
    def __init__(self):
        self.name = input('Enter the name : ')
        self.age = input('Enter the age : ')
        self.place = input('Enter the place : ')

    def show(self):
        print('Name : ', self.name, '\nAge : ', self.age, '\nPlace : ', self.place)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.id = int(input('Enter the stud ID : '))
        self.course = input('Enter the course : ')

    def show(self):
        super().show()
        print('------------Student-----------\nId : ', self.id, '\nCourse : ', self.course)


ob1 = Student()
ob1.show()
