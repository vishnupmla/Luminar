# 1. File create
# 2. File write
# 3. search a particular word in a file
# 4. Append new cintents
# 5. Delete a file
import re

# 1.

# f = open('my.txt','w')
# f.close()
# # 2.
# f = open('my.txt','w')
# f.write("THIS is my new file")
# f.close()
#
# f=open('my.txt','r')
# s = f.read()
# print(s)

# 3.
# f=open('my.txt','r')
# s = f.read()
#
# if 'my' in s:
#     print('Found')

# 4.
# f = open('my.txt','a+')
# f.write('\nThis is what I append to the file')
# f.seek(0)
# print(f.read())
# f.close()

# # 5.
# import  os
# os.remove('my.txt')

# 1. Write a program to find filenames with particular extension
#
# s="s.html,k.txt,m.jpeg,l.py,a.jpeg"
# t = re.search(r'[a-z]*.py',s)
# if t:
#     print(t.group())
# print(t)

# 2. Write a program to find words containing 'z' from a string
s="abcdz abzcd zabcd hjklj"

t = re.search(r'\b[a-z]*z[a-z]*\b',s)
print(t.group())