# 1.OBJECTIVE TYPE QUESTIONS
#
# Q.) def add_numbers(a, b):
#         return a + b
#
#     def multiply_numbers(a, b):
#         return a * b
#
#     result = add_numbers(2, 3) * multiply_numbers(2, 3)
#     print(result)
#     a) 10
#     b) 25
#     c) 30
#     d) 36
#answer
#     c) 30
# 2.THEORY TYPE QUESTIONS
#
# Q) What are the different types of inheritance ? and explain them
#answer
# 1. Single Inheritance
# A class inherits from one parent class, gaining access to its attributes and methods.
#
# 2. Multiple Inheritance
# A class inherits from more than one parent class, combining attributes and methods from all.
#
# 3. Multilevel Inheritance
# A class inherits from a parent class, which in turn inherits from another parent class, forming a chain.
#
# 4. Hierarchical Inheritance
# Multiple classes inherit from a single parent class, sharing common functionalities while having their own unique features.
#
# 5. Hybrid Inheritance
# A combination of two or more types of inheritance, providing a more complex and flexible structure.


# 3. CODING TYPE QUESTION
# Q)create this pattern using python?
#
#     ---
#     --- |
#     --- | ---
#     --- | --- |
#     --- | --- | ---
#     --- | --- |
#     --- | ---
#     --- |
#     ---
#answer
for i in range(1,6):
    for j in range(1,i+1):
        if j%2!=0:
            print("---",end=" ")
        else:
            print("|", end=" ")
    print()
for p in range(4,0,-1):
    for j in range(1,p+1):
        if j%2!=0:
            print("---",end=" ")
        else:
            print("|", end=" ")
    print()


# 4.APTITUDE TYPE QUESTIONS
#
# Q)Pointing to a photograph, a man says, "The woman in the photograph is the only daughter of my mother's brother." How is the man related to the woman in the photograph?
#
# a) Cousin
# b) Brother
# c)Uncle
# d)Nephew
#answer
# a) Cousin