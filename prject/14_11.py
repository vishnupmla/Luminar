# 1.  what is the output of the following code
# def test(a, b=2, c=3):
# return a + b + c
# print(test(1, c=5))

# ans : 8

# 2. What is the difference between remove(), pop(), and del when working
# with lists?

# remove() - it removes the first matching value from the list
# pop() - it removes the value from the index and return the deleted value
# del - it is used to delete any variable or list of values from a list

# 3. Write a python programme to find the numbers between 100 and 400(both
# included) where each digit of the number is an even number .The numbers
# obtained should print in a comma separated sequence

for i in range(100,401):
    f = 1
    for j in str(i):
        if int(j) % 2 != 0:
            f = 0
            break
    if f ==1:
        print(i,end= ',')

# 4. Two numbers are in the ratio 9:11 .If the sum of these two  numbers is 660,find the difference between these numbers

# 9x + 11x = 660
# 20x =660
# x = 660/20
# x =33
#
# 363-297 = 66
# ans = 66