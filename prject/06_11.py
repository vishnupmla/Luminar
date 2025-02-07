# 1.
# Objective
# type question
#
# Study
# the
# following
# program:
#
# a = 1
# while True:
#     if a % 7 = = 0:
#         break
#     print(a)
#     a += 1


# Which of the following is correct output of this program?

# a) 1 2 3 4 5
# b) 1 2 3 4 5 6
# c) 1 2 3 4 5 6 7
# d) Invalid

# answer - b)  1 2 3 4 5 6

# syntax
#
# 2.
# Theory based question
#
# Explain the different types of arguments in python?
#answer:
# 1) positional arguments
# 2) keyword argument
# 3) Default argument
# 4) Arbitrary arguments -> keyword type & non-keyword type


# 3. Coding based question

# Define a function to check whether a number is prime or not.
# answer

def check_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(num,'is a not prime number')
                break
        else:
            print(num,'is a prime number')
check_prime(int(input('Enter a number to check prime : ')))

# 4. Aptitude Based Question
#
# Two trains running in opposite directions cross a man standing on the platform in 27 seconds and 17
# seconds respectively and they cross each other in 23 seconds.The ratio of their speeds is:
# a) 1: 3
# b) 3: 2
# c) 3: 4
# d) None of these

# answer : b) 3: 2