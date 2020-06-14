# 1) є 4 функції :
#   add(x,y) : return x+y,
#   subt(x,y) : return x-y,
#   mult(x,y) : return x*y,
#   div(x,y) : return x//y
#
#   а) написати декоратор який рахує загальну кількість викликів усіх функцій
#   б) написати декоратор який в словник записує окремо скільки раз було викликано кожну функцію
# count = 0
# dic = {}
# def count_all(func):   ///////////////////task a
#     def wrap(*args, **kwargs):
#         global count
#         count += 1
#         return func(*args, **kwargs)
#     return wrap
#
# def count_single(func):   ///////////////////task b
#     count_s = 0
#     def wrap(*args, **kwargs):
#         nonlocal count_s
#         count_s += 1
#         dic[func.__name__] = count_s
#         return func(*args, **kwargs)
#     return wrap
#
# @count_all
# @count_single
# def add(x, y):
#     return x + y
# @count_all
# @count_single
# def subt(x, y):
#     return x - y
# @count_all
# @count_single
# def mult(x, y):
#     return x * y
# @count_all
# @count_single
# def div(x, y):
#     return x // y
#
# print(mult(2, 3))
# print(add(8, 9))
# print(div(5, 10))
# print(add(8, 9))
# print(div(5, 10))
#
# print(count)
# print(dic)
# ---------------------------------------------------------------------
# def decor(name):
#     def inner(func):
#         def wrap():
#             print(name)
#             func()
#             print('---------------')
#         return wrap
#     return inner
# def decor2(func):
#     def wrap():
#         print('***********')
#         func()
#         print('***********')
#     return wrap
#
# @decor('Alex')
# @decor2
# def func2():
#     print(2*5)
# func2()
# def st():
#     print('my function')
#
# get = decor('vasia')
# get = get(st)
# get()