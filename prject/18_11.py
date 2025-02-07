# 1. ans : d)

# 2. ans :
# break - Used to exit from a loop on reaching certain condition
# continue - Used to skip an iteration on reaching certain condition
# pass - Used to create a null block, we can create an empty block with pass keyword

# 3.

lst = []
def add_element():
    element = int(input('Enter the new element: '))
    lst.append(element)
    print('Element added to the list!!')

def search():
    key = int(input('Enter the element to search: '))
    for i in lst:
        if i == key:
            print('Element found',key)
        else:
            print('Element not found',key)

def display():
    print('----------Displaying List---------\n',lst)

while 1:
    print('Choose from the menu\n1. Add element to the list\n2. Search an element\n3. Display List\n4. Exit')
    ch = int(input('Enter the choice: '))

    if ch == 1:
        add_element()

    elif ch == 2:
        search()

    elif ch ==3:
        display()

    elif ch == 4:
        break

    else:
        print('Enter a valid choice!!')


