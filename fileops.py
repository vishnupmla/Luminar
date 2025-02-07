# # write a program to print number of lines in a file
# f = open('p.txt','r')
# cnt = f.readline()
# print(len(cnt))
#
# # write a program to print the number of letters, spaces and digits  in a file
#
# s = f.read()
# let = 0
# dig = 0
# spc = 0
# for i in s:
#     if i.isalpha():
#         let += 1
#     elif i.isdigit():
#         dig += 1
#     else:
#         spc += 1
# print('Number of letters = ',let)
# print('Number of digit = ',dig)
# print('Number of space = ',spc)


# write a program to append the content of one text file into another one
f = open('sample.txt','a+')
f1 = open('p.txt','r')
s = f1.read()
f.write(s)
print(f.read())
f.close()