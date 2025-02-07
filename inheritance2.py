# # Parent Vehicle child Car
# # Create 2 car objects and display details of car objects
# class Vehicle:
#     # Brand , Model, Color
#     # show()
#
#     def __init__(self):
#         self.brand = input('Enter the brand name: ')
#         self.model = input('Enter the model name: ')
#         self.color = input('Enter the color: ')
#
#     def show(self):
#         print('Brand name : ',self.brand)
#         print('Model name : ',self.model)
#         print('Color : ',self.color)
#
# class Car(Vehicle):
#     # CC
#     # Show
#     def __init__(self):
#         super().__init__()
#         self.cc = int(input('Enter the Engine CC: '))
#
#     def show(self):
#         super().show()
#         print('Engine Capacity = ',self.cc)
#
# ob1 = Car()
# ob1.show()
#
# ob2 = Car()
# ob2.show()




# ========================================================

# class Parent1:
#     def f1(self):
#         print('f1 from parent class 1')
#
# class Parent2:
#     def f2(self):
#         print('f2 from parent class 2')
#
# class Child(Parent1,Parent2):
#     pass
#
# ob = Child()
# ob.f1()
# ob.f2()






# ======================================================================================================================

# class Hospital:
#     def __init__(self):
#         self.hosname = input('Enter the hospital name: ')
#         self.location = input('Enter the location: ')
#         self.phone = int(input('Enter the phone number: '))
#
#     def show(self):
#         print('Hospital Name = ',self.hosname)
#         print('Location = ',self.location)
#         print('Phone number = ',self.phone)
# class Department:
#     def __init__(self):
#         self.dep_name = input('Enter the department name: ')
#         self.dr_name = input('Enter the doctor name: ')
#
#     def show(self):
#         print('Department name = ',self.dep_name)
#         print('Doctor name = ',self.dr_name)
#
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#
#         self.patient_name = input('Enter the patient name: ')
#         self.age = int(input('Enter the age: '))
#         self.gender = input('Enter the gender: ')
#         self.place = input('Enter the place: ')
#
#     def show(self):
#         Hospital.show(self)
#         Department.show(self)
#
#         print('Patient name = ',self.patient_name)
#         print('Age of patient = ',self.age)
#         print('Gender = ',self.gender)
#         print('Place = ',self.place)
#
# ob = Patient()
# ob.show()


'''
 Polymorphism
-----------------------------

poly-morphs ( many form)

in python
method overloading
method overriding
operator overloading

method overloading
-> allows to define multiple methods with same name, but with different parameters in the same class

python doesnot support Method overloading, but can be achieved with arbitrary arguments *args ands *kwargs


with the use of args and kwargs
'''

# =====================================================================================================================

class A:
    # def f1(self):
    #     print('f1 with no arguments')
    #
    # def f1(self,a1):
    #     print('f1 with 1 argument',a)
    #
    # def f1(self,a,b):
    #     print('f1 with 2 arguments',a,b)

    def show(self,a=0,b=0):
        if (a==0 and b == 0):
            print('No values')
        elif b==0:
            print('value of a ',a)
        else:
            print('value of a and b : ',a,b)

a= A()
# a.f1(2,4)
a.show()
a.show(2)
a.show(4,5)
