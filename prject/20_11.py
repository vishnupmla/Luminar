 #1. What will be the output of the following Python code?
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k =foo()
# print(k)


 # ans : b) 2

 # 2. What is the difference between iterable and iterator variables?

 # iterable - An Iterable is basically an object that any user can iterate over.
 # iterator - An Iterator is also an object that helps a user in iterating over another object that is iterable.


# 3.    Write a function that checks if two strings are anagrams of each other.

def check_anagrams(word1, word2):
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            print(word1,'is an ANAGRAM of',word2)

        else:
            print(word1,'is not an ANAGRAM of',word2)
    else:
        print(word1,'is not an ANAGRAM of',word2)

check_anagrams('listen','silent')


#4. A shopkeeper sells a book at ₹120, making a profit of 20%. What is the cost price of the book?

# 20 % CP + CP =120
# 20/100 * CP + CP =120
# 0.2CP + CP =120
# 1.2CP = 120
# CP = 120 / 1.2 = 100
#
# ans : b)

