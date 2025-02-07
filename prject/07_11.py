# 1. *args are stored as tuple

# 2. List                                                 |         tuple
# --------------------------------------------------------|---------------------------------------------------------
# * List is a collection of heterogeneous elements        | Tuple is also collection of heterogeneous elements
# * List is declared using square brackets                | Tuple is declared inside parentheses
# * List is mutable                                       | Tuple is immutable
# * Elements can be accessed using indexing               | Indexing is not allowed
#

# 3. Function to check whether a number is armstrong or not

def check_armstrong(num):
    l = len(str(num))
    str_num = str(num)
    rslt = 0
    for i in str_num:
        rslt += int(i)**l
    if rslt == num:
        print(num,'is an armstrong number')
    else:
        print(num,'is not an armstrong number')

check_armstrong(int(input('Enter the number: ')))

# 4. Train length = 300m
#     speed = 54km/hr
#     time taken to cross a telephone post

# s =d/t
# t = d/s
#
# d = 300
# s = 54 * 5/18 = 15 m/sec
#
# t = 300 / 15
# t = 20 sec