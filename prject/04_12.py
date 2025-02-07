# 1) OBJECTIVE TYPE QUESTION
#
#    Study the following statements:
# 	x = [1, 2, 3, 4]
# 	print(x[1:3])
#
#    What will be the output of this statement?
#
#   a) [1, 2]
#   b) [2, 3]
#   c) [3, 4]
#   d) Error

# ans : b)

# 2)THEORY BASED QUESTION
#
#   What does the __init__ method do in Python?

# ans : __init__() act as constructor method in python, used to initialize attributes when an object is created

# 3)CODING TYPE QUESTION
#   Write a python program to print the following pattern
#
#   h e l l o
# 	h e l l
# 	h e l
# 	h e
# 	h

s = 'hello'
for i in range(len(s),-1,-1):
    for j in range(i):
        print(s[j], end=' ')
    print()


#4. A box contains 5 red balls, 3 green balls, and 2 blue balls. If one ball is randomly picked, what is the probability that it is:
	#
	# 1)A red ball?
	# 2)Not a green ball?
 #
 #  A. (1) 0.4, (2) 0.6
 #  B. (1) 0.5, (2) 0.7
 #  C. (1) 0.3, (2) 0.5
 #  D. (1) 0.6, (2) 0.8

 '''
 ans: B)
 total = 5+3+2 = 10
 
 i) 5/10 = 0.5
 ii)7/10 = 0.7
 
 
 '''