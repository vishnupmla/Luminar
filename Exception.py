# try:
#     n1 = int(input('Enter the first number'))
#     n2 = int(input('Enter the second number'))
#
#     rslt = n1/n2
#
# except:
#     print('Division by zero is not allowed')
#     print('Reenter the inputs')
#
#
# else:
#     print('result = ',rslt)
import math

# Write a program that takes a number as input from the user and find factorial of that number using math.factorial
# use try except block handle the value error if user input negative / character as input

# try:
#     num = input('Enter the number to find factorial')
#     print('Factorial = ',math.factorial(num))
# except:
#     if num < 0:
#         print('Negative numbers cannot have factorial')
#     elif type(num) != int:
#         print('The number is not an integer')
#     else:
#         pass


# write a program to open a file in read mode  if the file doesnot exist  catch the exception and print

# try:
#     f = open('t.txt','r')
# except:
#     print('File doesnot exist')




try:
    n1 = int(input('Enter the first number'))
    n2 = int(input('Enter the second number'))

    rslt = n1/n2

# except ZeroDivisionError as z:
#     # print('Division by zero is not allowed')
#     print(z)
# except ValueError as v:
#     print(v)
#     # print('Invalid input')
except Exception as e:
    print(e)
    # print('Error occurred')

else:
    print('result = ',rslt)