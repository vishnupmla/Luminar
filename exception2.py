# import math
#
# def find_fact():
#     try:
#         num = int(input('Enter the number to find factorial'))
#         rslt = math.factorial(num)
#     except Exception as e:
#         print(type(e),'',e)
#         find_fact()
#     else:
#         print(rslt)
#
# find_fact()
#
#
#
# while True:
#     try:
#         num = int(input('Enter the number to find factorial'))
#         rslt = math.factorial(num)
#     except Exception as e:
#         print(type(e),'',e)
#         find_fact()
#     else:
#         print(rslt)
#         exit()
#
#

# num = int(input('Enter a positive number'))
# if num < 0:
#     raise Negativeerror('Enter a positive number')

def __add__(self,other):
    self.x+


def validate_age(age):
    if age<0:
        raise ValueError('Age cannot be negative')
    elif age>120:
        raise ValueError('Age is invalid')
    else:
        print('Age is valid')

validate_age(int(input('Enter the age : ')))