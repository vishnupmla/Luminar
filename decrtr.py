# def chng_div(func):
#
#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#         func(a,b)
#     return inner
#
# @chng_div
# def div(a,b):
#     print(a/b)
# div(3,9)
# # dcr = chng_div(div)
# # dcr(2,4)



# def test(func):
#     def wrapper(a,b):
#         if a<b:
#             a,b = b,a
#         func(a,b)
#
#     return wrapper
#
# def div(a,b):
#     print(a/b)
#
# val = test(div)
# val(4,8)

# def upper(func):
#     def wrapper():
#         fun = func()
#         mak = fun.upper()
#         print(mak)
#     return wrapper()
#
# @upper
# def getstring():
#     return 'lmo'




def make_change(func):
    def wrapper(*args):
        print("Start")
        args = list(args)
        if args[0] < args[1]:
            args[0],args[1] = args[1],args[0]
            func(*args)
        print("End")
    return wrapper
@make_change
def div(a,b):
    print(a/b)

div(4,32)


