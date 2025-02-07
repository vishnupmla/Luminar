# Menu driven code for file operations
import os

# 1. File create
# 2. File write
# 3. search a particular word in a file
# 4. Append new cintents
# 5. Delete a file

def create_file(file_name):
    f = open(file_name,'w')
    f.write(input('Enter the content to be added to the file:\n'))
    f.close()

def read_file(file_name):
    try:
        f = open(file_name,'r')
        # f.write(input('Enter the content to be added to the file:\n'))
        # f.seek(0)
        print('-------content of the file--------\n',f.read())
    except:
        print('File doesnot exist')
    else:
        pass

def search_word(filename,key):
    f = open(filename,'r')
    s = f.read()
    if key in s:
        print('The word found in the context!!')
    else:
        print('The word not exist!!')

def append_content(filename):
    with open(filename,'a+') as f:
        f.write(input('Enter the content to be added \n  '))
        f.seek(0)
        print('---------The content of the file----------\n',f.read())
        f.close()

def delete_file(filename):
    try:
        os.remove(filename)
        print('The file is removed')
    except:
        print('Check the file name, file may not exist!!')
    else:
        pass

while True:
    print('Enter the operation you want to perform')
    print('1. File write\n2. File read\n3. Search a particular word in a file\n4. Append new contents\n5. Delete a file\n6. Exit')
    ch = int(input('Enter the choice : '))

    if ch == 1:
        create_file(input('Enter the filename with extension: '))

    elif ch == 2:
        read_file(input('Enter the filename with extension: '))

    elif ch == 3:
        search_word(input('Enter the filename with extension: '),input('Enter the word to be searched: '))

    elif ch == 4:
        append_content(input('Enter the filename with extension: '))

    elif ch == 5:
        delete_file(input('Enter the filename with extension: '))

    elif ch == 6:
        break
    else:
        print('Enter a valid choice')