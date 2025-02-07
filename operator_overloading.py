# # Magic methods
# class A:
#     def __init__(self):
#         self.x = int(input('Enter a num: '))
#         self.y = int(input('Enter a num: '))
#
#     def __add__(self, other):
#         return (self.x + other.x)+(self.y+other.y)
#
#     def __sub__(self, other):
#         return (self.x - other.x)
#
#     def __mul__(self, other):
#         return self.x * other.x
#
#     def __div__(self, other):
#         return self.x/other.x
#
# ob = A()
# ob1 = A()
#
# print(ob+ob1)
# print(ob-ob1)
# print(ob*ob1)
# print(ob/ob1)


# __str__(self)
# ---------------------------------

class B:
    def __str__(self):
        return 'Object created'

b = B()
print(b)

from abc import ABC,abstractmethod