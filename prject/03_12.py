# 1. # def func(a, b=[]):
#     b.append(a)
#     return b
#
# print(func(1))
# print(func(2))
# print(func(3, []))
# print(func(4))

# ans : a)

# 2. ans :
# Global - Refers to variables in the global namespace
# nonlocal -Refers to variables in the nearest enclosing function

# 3) CODING TYPE QUESTION
# Write a Python program to find all non-repeating character in a given string that occur at even indices.
# string="aabbbccdeeffghi"

# ans :
string="aabbbccdeeffghi"
for i in string:
    if string.count(i) == 1 and string.index(i)%2 == 0:
        print(i)


# 4) APTITUDE TYPE QUESTION
# A man can paddle a boat 30 km downstream in 3 hours and 18 km upstream in 3 hours. What is his speed in still water?
#
# Options:
# a) 6 km/h
# b) 7 km/h
# c) 8 km/h
# d) 9 km/h

'''
s + x = 10
s - x = 6   
(s + x)+(s - x) = 10+6
2s = 16
s = 8

ans :  8
'''

