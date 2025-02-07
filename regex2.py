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
#
# #Find all words starting with s,p or r and ends at 'at
# s="sat mat pat cat rat bat"
# p1 = r'[spr]at'
# print(re.findall(p1,s))
# #Find all words starting with except s,p or r and ends at 'at'
# s="sat mat pat cat rat bat"
# p2 = r'[^spr]at'
# print(re.findall(p2,s))
# # #Find all 3,4 and 5 digit numbers from the string
# s="123 6738 34556 355666 76767564 445222"
# p3 = r'\b[0-9]{3,5}\b'
# print(re.findall(p3,s))
#
# # -------------------> \b : Word boundary , \b exactly same as \W
#
# # #Find all 3,4 and 5 letter words from the string
# #
# s="The quick brown fox jumps over the lazy dog"
# p4 = r'[a-z]{3,5}'
# print(re.findall(p4,s))
#
# test = 'hello world,hello,world  _hello_world 12hello123'
# print(re.findall(r'\bhello\b',test))




# =====================================================================================================================



import re

# s = 'hello world python'
# m = re.match(r'hello',s)
# if m:
#     print('Match found')
#     print(m.group())
# else:
#     print('match not found')



s1 = 'hello world , hi python'
m1 = re.search(r'[lo]$',s1)

if m1:
    print('Match found --------- ',m1.group())
else:
    print('Not found')



# s2 = 'hello world , hi python'
# m = re.findall(r'h[a-z]+',s2)
# m1 = re.findall(r'\bh[a-z]+\b',s2)
# print(m)
# print(m1)


# s = 'john@abc.com and mike@pqr.com'
# m = re.sub(r'@[a-z]+','@gmail',s)
# print(m)


# s = 'python is a programming language'
# m = re.split(r'\s',s)
# print(m)
# m1 = re.split(r'p',s)
# print(m1)



# 1. Write a program to find filenames with particular extension
#       s="s.html,k.txt,m.jpeg,l.py,a.jpeg"

# 2. Write a program to find words containing 'z' from a string
#        s="abcdz abzcd zabcd hjklj"

# 3. Check whether the given string contains only lowercase, uppercase,digits and underscore
#        s="fghjkljhj6789087689_6 355"

# 4. Write a program to extract year/month/date from a url
#        s="www.washingtonpost.com/news/football-insider/wp/2016/09/02"

# 1
s="s.html,k.txt,m.jpeg,l.py,a.jpeg"
m = re.findall(r'[a-z]*.jpeg',s)
print(m)


# 2
s="abcdz abzcd zabcd hjklj"
m = re.findall(r'\b[a-z]*z[a-z]*\b',s)
print(m)

# 3
s="fghjkljhj6789087689_6 355"

m = re.search(r'^\W+$',s)
if m:
    print('Yes')
    # print(m.group())
else:
    print('No')

# 4
# Write a program to extract year/month/date from a url

s="www.washingtonpost.com/news/football-insider/wp/2016/09/02"

m = re.search(r'\d{4}/\d{2}/\d{2}',s)
print(m.group())



# 1.Replace \n with space
#
s="""Keep the blue flag
flying high
Chelsea"""
# output:Keep the blue flag flying high Chelsea
#

m1 = re.sub(r'\n',' ',s)
print(m1)


#
# Q2.Replace dot,comma and space  with :
s="Python is a,Programming language."
# output:"Python:is:a:Programming:language:"
# #

m2 = re.sub(r'[.,\s]',':',s)
print(m2)

# Q3.Remove all alphanumeric characters from the string
s="adfsgdhvj5678 &#%%^&& sfdhfhj _RfGGGG"
# output:" &#%%^&&  _"

m3 = re.sub(r'\w','',s)
print(m3)

# Q4.Find all words starting with vowel and ends with vowel from the given string
#
s="red green orange"
# output:orange

m4 = re.findall(r'[aeiou][a-z]+[aeiou]',s)
print('Words starting and ending with vowels = ',m4)


# Q5.Find the count of numbers in the string
s="One 1 two 2 three 3 four 4"
# output:4

m5 = re.findall(r'\d',s)
print('Count of numbers = ',len(m5))
