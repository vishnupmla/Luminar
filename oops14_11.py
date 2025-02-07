# create class Acoount and attributes account)number,name,balance
# methods withdraw, deposit, showbalance

# class Account:
#     def __init__(self):
#         self.acc_num = int(input('Enter the account number: '))
#         self.acc_name = input('Enter the name: ')
#         self.balance = 0
#
#     def deposit(self):
#         amnt = int(input('Enter the amount to deposit: '))
#         self.balance = self.balance + amnt
#
#     def withdraw(self):
#         if self.balance <= 0:
#             print('No balance available!!')
#         else:
#             amnt = int(input('Enter the amount to withdraw: '))
#             if amnt > self.balance:
#                 print('No available balance, please enter a amount less than or equal to your available balance of',
#                       self.balance)
#                 self.withdraw()
#             else:
#                 self.balance = self.balance - amnt
#                 print('Amount withdrawn ----', amnt)
#                 self.show_balance()
#
#     def show_balance(self):
#         print('Available balance in your account =', self.balance)


# ob1 = Account()
# ob1.deposit()
# ob1.show_balance()
# ob1.withdraw()


# ===================================================================================================================

# Menu driven

# class Account:
#     def __init__(self):
#         self.acc_num = int(input('Enter the account number: '))
#         self.acc_name = input('Enter the name: ')
#         self.balance = 0
#
#     def deposit(self):
#         amnt = int(input('Enter the amount to deposit: '))
#         self.balance = self.balance + amnt
#
#     def withdraw(self):
#         if self.balance <= 0:
#             print('No balance available!!')
#         else:
#             amnt = int(input('Enter the amount to withdraw: '))
#             if amnt > self.balance:
#                 print('No available balance, please enter a amount less than or equal to your available balance of',
#                       self.balance)
#                 self.withdraw()
#             else:
#                 self.balance = self.balance - amnt
#                 print('Amount withdrawn ----', amnt)
#                 self.show_balance()
#
#     def show_balance(self):
#         print('Available balance in your account =', self.balance)
#
# lst = []
#
# # for i in lst:
#
#
# while True:
#     print('----------Enter the operation you want to perform---------')
#     print('1. Create Account\n2. Withdraw\n3. Deposit\n4. Show Blanace\n5. Exit')
#     ch = int(input('Enter your choice: '))
#     if ch == 1:
#         ob1 = Account()
#         lst.append(ob1)
#
#     elif ch == 2:
#         num = int(input('Enter the account number: '))
#         for i in lst:
#             if (i.acc_num == num):
#                 i.withdraw()
#                 break
#         else:
#             print('Account number doesnot exist!!')
#
#     elif ch == 3:
#         num = int(input('Enter the account number: '))
#         for i in lst:
#             if (i.acc_num == num):
#                 i.deposit()
#                 break
#         else:
#             print('Account number doesnot exist!!')
#
#     elif ch == 4:
#         num = int(input('Enter the account number: '))
#         for i in lst:
#             if (i.acc_num == num):
#                 i.show_balance()
#                 break
#         else:
#             print('Account number doesnot exist!!')
#
#     elif ch == 5:
#         exit()
#     else:
#         print('Enter a Valid choice!!')
#
#     print(lst)



# Write a menu driven code

# 1. Add Book
# 2. Show book list
# 3. show details of a book
# 4. Update book
# 5. Delete book

class Books:
    def __init__(self):
        self.book_name = input('Enter the name of the book: ')
        self.author = input('Enter the author name: ')
        self.genre = input('Enter the genre of the book: ')
        self.publisher = input('Enter the publisher name: ')
        self.price = int(input('Enter the price: '))

    def show_details(self):
        print('------------Book details-------------')
        print('Book Name : ',self.book_name,'\nAuthor : ',self.author,'\nGenre : ',self.genre,'\nPublisher : ',self.publisher,'\nPrice : ',self.price)

    def update(self):
        attr = input('Enter the choice: Book_name/Author/Genre/Publisher/Price/all')
        if attr == 'all':
            self.book_name = input('Enter the updated book name: ')
            self.author = input('Enter the updated author name: ')
            self.genre = input('Enter the updated genre of the book: ')
            self.publisher = input('Enter the updated publisher name: ')
            self.price = int(input('Enter the updated book price: '))
        elif attr == 'Book_name':
            self.book_name = input('Enter the updated book name: ')
        elif attr == 'Author':
            self.author = input('Enter the updated author name: ')
        elif attr == 'Genre':
            self.genre = input('Enter the updated genre of the book: ')
        elif attr == 'Publisher':
            self.publisher = input('Enter the updated publisher name: ')

        elif attr=='price':
            self.price = int(input('Enter the updated book price: '))

        else:
            print('Enter a valid choice')
            self.update()
lst = []
while 1:
    print('\n\n----------Choose from the menu---------')
    print('1. Add Book\n2. Show Book List\n3. Show details\n4. Update Book\n5. Delete Book\n6. Exit')
    ch = int(input('Enter the choice: '))

    if ch == 1:
        ob = Books()
        lst.append(ob)

    elif ch == 2:
        print('------------Book List------------')
        for i in lst:
            print('*',i.book_name)

    elif ch == 3:
        name = input('Enter the Book name: ')
        for i in lst:
            if i.book_name == name:
                i.show_details()
                break
            else:
                print('No matching Book')
    elif ch == 4:
        name = input('Enter the name of book you want to update: ')
        for i in lst:
            if i.book_name == name:
                i.update()
                break
            else:
                print('No match found!!')


    elif ch == 5:
        print('------------Book List------------')
        for i in lst:
            print('*',i.book_name)

        name = input('\n\nEnter the Book you want to delete: ')
        for i in lst:
            if i.book_name == name:
                lst.remove(i)
                break
            else:
                print('No matching Book')

    elif ch == 6:
        exit()

    else:
        print('Enter a valid choice!!')