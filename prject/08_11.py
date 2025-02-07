#1. ------- a)

# 2

# 3. Find the most frequent characters in a string
str = input('Enter a string: ')
dct = {}
for i in set(str):
    dct[i] = str.count(i)
print(dct.items())

# 4. 