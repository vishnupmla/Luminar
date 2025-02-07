# def countOddEvenDifference(n,lst):
#     odd_cnt = 0
#     evn_cnt = 0
#     for i in lst:
#         if i % 2 == 0:
#             evn_cnt += 1
#         else:
#             odd_cnt += 1
#     return odd_cnt - evn_cnt
#
# print(countOddEvenDifference(8,[10,20,30,40,55,66,77,83]))

# --------------------------------------------------------------------------------------------

# def findTotalSum(n,lst,pos):
#     sum = 0
#     for i in range(pos-1,n-1):
#         sum += abs(lst[i] - lst[i+1])
#     return sum
# lst = list(map(int,input().split()))
# print(findTotalSum(7,[11,22,12,24,13,26,14],5))

# -------------------------------------------------------------------------------------------------

# def findDifference(n,lst):
#     evn, odd = 0, 0
#     for i in range(0,n):
#         if i % 2 == 0:
#             evn += lst[i]
#         else:
#             odd += lst[i]
#     # print(max(odd,evn),min(odd,evn))
#     return max(odd,evn) - min(odd,evn)
#
# print(findDifference(7,[10,20,30,40,50,60,70]))
# 160 - 120

# -----------------------------------------------------------------------------------------------

# def findTotalCurtains(n,lst):
#     cnt = 0
#     for i in lst:
#         cnt += i//12
#     return cnt
# print(findTotalCurtains(5,[3,42,60,6,14]))


# ---------------------------------------------------------------------------------------------------

# def countOfDigit(num):
#     cnt = 0
#     s = str(num)
#     st =set(s)
#     for i in st:
#         if s.count(i) > 1:
#             cnt += 1
#     return cnt
# print(countOfDigit(121342))


# ------------------------------------------------------------------------------------------------------

# def findTotalDistance(n,lst):
#     sm = 0
#     for i in range(0,n-1):
#         sm += abs(lst[i] - lst[i+1])
#     return sm
# print(findTotalDistance(5,[10,11,7,12,14]))

# -------------------------------------------------------------------------------------------------------------

n = 25143
k = 3
s = str(n)
print(s[3:]+s[:3])