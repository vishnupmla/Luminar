# 1. Objective Type
# What is the output of the following code?
# print(bool(0), bool(1), bool(-1))
# a) False True True
# b) False True False
# c) True False True
# d) True True True

# ans : a)

# 2.Theory Based
# what is the difference between method overloading and method overriding?

'''
Method overloading in which methods with same name but different number of parameters can be defined and used inside a class
python support method overloading using default parameters and arbitrary methods

Method overriding in which methods defined in parent class can be redefined inside child class either for extending or define inside child class
super() method is used for overriding functions

'''

# 3. Create a base class Shape with an area() method, and derived classes Circle, Rectangle, and Triangle
# to calculate their respective areas.
from abc import abstractmethod,ABC
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,):
        self.rad = int(input('Enter the radius of the Circle: '))

    def area(self):
        ar = 3.14*self.rad*self.rad
        print("Area of circle = ",ar)

class Rectangle(Shape):
    def __init__(self):
        self.len = int(input('Enter the Length of Rectangle: '))
        self.bre = int(input('Enter the Breadth of Rectangle: '))

    def area(self):
        ar = self.len * self.bre
        print('Area of Rectangle = ',ar)

class Triangle(Shape):
    def __init__(self):
        self.base = int(input('Enter the base length of Triangle: '))
        self.hei = int(input('Enter the height: '))

    def area(self):
        ar = 0.5 * self.base *self.hei
        print('Area of Rectangle = ',ar)

ob1 = Circle()
ob1.area()

ob2 = Rectangle()
ob2.area()

ob3 = Triangle()
ob3.area()

# 4. A car covers a distance of 360 km in 6 hours. If its speed is reduced by 10 km/hr, how much more
# time will it take to cover the same distance?

'''
ans : 
sp = d/t
sp = 360 / 6
sp = 60 km/Hr

when sp = 50
t = d/sp
  = 360 / 50
  = 7.2 Hrs
'''
