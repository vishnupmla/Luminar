# import re
#
# s = '''John is 35 and Sam is 25
#     Mike is 20 and Joseph is 80'''
#
# nameptrn = '[A-Z][a-z]+'
# names = re.findall(nameptrn,s)
# print(names)
#
# agepatrn = '[0-9]{2}'
# ages = re.findall(agepatrn,s)
# print(ages)
import re

# s = 'abd abcd abccd abcccd abed'
#
# p1 = r'abc+d' # + - 1 or more ocur of c
# print(re.findall(p1,s))
#
# p2 = r'abc*d'  # * 0 or more ocur of c
# print(re.findall(p2,s))
#
# p3 = r'abc?d'  # ? - exactly 0 or 1
# print(re.findall(p3,s))
#
# p4 = r'abc{1,3}d'
# print(re.findall(p4,s))
#
# p5 = r'abc+d' # + - 1 or more ocur of c
# print(re.findall(p1,s))

#Find all words starting with s,p or r and ends at 'at
s="sat mat pat cat rat bat"
p1 = r'[spr]at'
print(re.findall(p1,s))
#Find all words starting with except s,p or r and ends at 'at'
s="sat mat pat cat rat bat"
p2 = r'[^spr]at'
print(re.findall(p2,s))
# #Find all 3,4 and 5 digit numbers from the string
s="123 6738 34556 355666 76767564 445222"
p3 = r'\b[0-9]{3,5}\b'
print(re.findall(p3,s))

# -------------------> \b : Word boundary , \b exactly same as \W

# #Find all 3,4 and 5 letter words from the string
#
s="The quick brown fox jumps over the lazy dog"
p4 = r'[a-z]{3,5}'
print(re.findall(p4,s))

test = 'hello world,hello,world  _hello_world 12hello123'
print(re.findall(r'\bhello\b',test))