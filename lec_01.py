# for i in range(10):
#     if i == 5 or i == 6 or i == 1:
#         continue
#     print(i)
# ------string------------------
# st = 'Hello, world!'
# print(st[::-1])
# st = '222111255'
# print(st.rfind('dd'))
# st = '122333'
# print(st.isspace())
# st  = r'hello \tworld'
# print(st)
# st = '"hello"\'\''
# print(st)
# name = 'Ihor'
# age = 28
# print('name = %(name)s \nage = %(age)s' % {'name': name, 'age': age}) # 1 method
# print('name = {0} \nage = {1}'.format(name, age)) # 2 method
# print('name = {n} \nage = {a}'.format(a=age, n=name))  # 2 method
# print(f'name = {name.center(6,"*")} \nage = {age-2}')  # 3 method
# -----list---------------
# l1 = [1, 2]
# l2 = l1 # link to l1
# print(l1)
# print(l2)
# l1[0] = 55
# print(l1)
# print(l2)
# -------------------------------
# l1 = [1, 2]
# # l2 = list(l1) # copy to l1
# l2 = l1[:] # copy to l1
# print(l1)
# print(l2)
# l1[0] = 55
# print(l1)
# print(l2)
# -------------------------------
# list = [1, 2, 3, 4, 5]
# print(1 in list)
# if 1 in list:
#     del list[0]
# print(list)
# print(11 not in list)
# ------methods list-------------
# list = [1, 2, '3', 4, 5]
# list1 = list.copy()
# list[0] = 0
# print(list)
# print(list1)
# list.append(88)
# print(list)
# list.insert(2, 99)
# print(list)
# del list[0]
# print(list[0])
# x = list.pop()  # delete end element
# print(x * 2)
# list.pop(2) # delete index element
# # # print(list)
# list.remove('3') # delete value
# print(list)
# l1 = [1, 2]
# # l2 = [2, 3]
# # l1.extend(l2)
# # print(l1)
# list = [1,5,8.5,4.5,9,7]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# ---------tuple-----------------
# t = (1, 2, 3, 4)
# l = [1, 2, 3, 4]
# print(t.__sizeof__()) # size_t < size_L
# print(l.__sizeof__())
# --------dict------------------
# d = {'name': 'Bob', 'age': 36}
# # print(d['name'])
# d = dict([('name', 'Bob'), ('age', 36)])
# print(d)
# d = dict.fromkeys(['www', 1, 2], 1111)
# print(d)
# ---------dict methods-------------
# d = {'name': 'Bob', 'age': 25, 11: 333}
# # print(d.get('name'))
# # print(d.popitem())
# d.setdefault('login')
# print(d)
# ---------set-------------------------
# s = {1, 11, 5, 5, 5, 5, 5, 5, 44, 88, 6}
# print(s)
# s.add(2.2)
# print(s)
# s.pop()
# print(s)
# s.discard(1)
# print(s)
# s.discard(55)
# print(s)
# set = frozenset({1,2,5,6,4,8}) # not delete element = tuple
# ----------------methods set----------------
# set1 = {1, 2, 31, 41, 51}
# set2 = {1, 2, 3, 4, 5}
# print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)
# print(set1)
# print(set1.difference(set2))
# set1.difference_update(set2)
# print(set1)
# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1)
# s = set1.union(set2)
# print(s)
# set1 = {1, 2, 31, 41, 51}
# set2 = {1, 2}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
# set1 = {11, 22, 33}
# set2 = {1, 2, 3}
# print(set1.isdisjoint(set2))
# ----------function-------------
# def some(n1, n2=2):
#     return n1 + n2
# print(some(5))
# def some(*args):
#     return args
# print(some(3,5,4,8,9))
# print(some())
# def some(name, mail='gmail', *args, **kwargs):
#     print(name)
#     print(mail)
#     print(args)
#     print(kwargs)
#
#
# some('Bob', 'gmail', 1, 5, age=25, www='www')
# ---------------------------------------------------
