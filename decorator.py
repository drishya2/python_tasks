# def decorator(func):
#     def prnt():
#         print('hi all')
#         func()
#         print('bye all')
#     return prnt
#
#
#
#
# @decorator
# def func():
#     print('how is everything')
#
#
# func()
#


def dec(func):
    def divide(a,b):
        if b>a:
            a,b=b,a
            func()


@dec
def func(a,b):
    print(a/b)

func(4,2)