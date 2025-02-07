# 1. Objective Type
#
# Which of the following is not a valid keyword in Python?
#
# a) def
#
# b) class
#
# c) continue
#
# d) include

# ans : d)

# 2.Theory Based
#
# What are looping control statements? Explain them

# ans : break - use to exit fromm the loop on meeting certain condition
#       continue - used to skip an iteration on reaching certain condition
#       pass - used to create a null block


# 3.Coding Type Question
#
# Print the pattern given below
#
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# ans :
rows = 5

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

for i in range(rows-1, 0, -1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

    # 4.
    # Aptitude
    # Type
    # Question
    #
    # What is the next number in the series: 2, 6, 12, 20, 30, ___?
    #
    # a) 40
    #
    # b) 42
    #
    # c) 44
    #
    # d) 46

# ans : b)