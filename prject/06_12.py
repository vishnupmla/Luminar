# 1.OBJECTIVE TYPE QUESTIONS
#
# Q.)  Which library in Python is used for numerical computations?
#
# A) Matplotlib
# B) Numpy
# C) Pandas
# D) Scikit-learn
#
# 2.THEORY TYPE QUESTIONS
#
# Q) Explain the difference between deep copy and shallow copy in Python.
#
# 3. CODING TYPE QUESTIONS
#
# Q)Write a Python function that checks if a given year is a leap year.
#
# 4.APTITUDE TYPE QUESTIONS
# Q)5. Speed and Distance
# A car travels 180 km at a speed of 60 km/h. How long does it take to complete the journey?
#
# a) 2 hours
# b) 3 hours
# c) 4 hours
# d) 5 hours

# 1. B
# 2. A shallow copy creates a new object, but does not create copies of the objects that the original
# object references. Instead, it copies references to those objects.

# A deep copy creates a completely independent copy of the object and all objects it references.
# Changes to the deep-copied object do not affect the original object, and vice versa.

# 3.
yr = int(input('Enter a year: '))
if yr %4 == 0 and yr%100 != 0 or yr%400==0:
    print('The year is a leap year')
else:
    print('The year is not leap year')

# 4. s = d/t
#    t = d/s
#       = 180/60 = 3hrs