# 1.Objective Type Questions
# a = [1, 2, 3, 4]
# b = [sum(a[0:x+1]) for x in range(0, len(a))]
# print(b)
# a) [1, 2, 3, 4]
# b) [1, 3, 6, 10]
# c) [10, 6, 3, 1]
# d) [4, 3, 2, 1]

# ans : b)

# 2. What are the differences between append(), extend(), and insert() in a Python list?

# append method is used to add value at the end of the list
# Extend() is used to append a set of iterable to the end of the list
# insert is used to add elements at the desired index position

# 3. You have a list of integers. Write a Python function to find all pairs of numbers that sum to a
# specific target.

lst = [1,2,3,4,5,6]
for i in range(len(lst)):
    for j in range(len(lst)):
        if i==j:
            continue
        if lst[i] + lst[j] == 10:
            print((lst[i], lst[j]))

# 4. What is the next number in the series: 2, 6, 12, 20, __?

# ans : a)30