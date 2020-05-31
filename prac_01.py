# Task 1
# 1) написати прогу яка переводить температуру в С в F і навпаки
#   Формули - С to F : F=C*1.8+32
#       - F to C : C=(F-32)/1.8
# C = 20
# F = 50
# temp_F = C * 1.8 + 32
# temp_C = (F - 32) / 1.8
# print(temp_F)
# print(temp_C)
# Task 2
# 2) перевірка числа чи воно додатнє чи від'ємне, не забуваємо,
#   що є ще 0
# ------------------------------------------
# x = 5
# if x > 0:
#     print('positive number')
# elif x < 0:
#     print('negative number')
# else:
#     print('zero')
# Task 3
# 3) вивести найбільше число з трьох чисел
# ------------------------------------------
# x = 5
# y = 18
# z = 12
# if  x > y and x > z:
#     print('max_number',x)
# elif y > x and y > z:
#     print('max_number',y)
# else:
#     print('max_number',z)
# Task 4
# 4) вивести суму цифр трьохзначного числа,
#   наприклад: 123 = 6; 111 = 3; 333 = 9
# x = 123
# num_1 = x // 100
# num_2 = (x % 100) // 10
# num_3 = (x % 100) % 10
# sum_num = num_1 + num_2 + num_3
# print(sum_num)
# ------------------------------------------
# a = 345
# sum = 0
# while a:
#     sum += a % 10
#     a //= 10
# print(sum)
# Task 5
# 5) вивести на екран пустий квадрат з зірочок з довжиною сторін, яка вказана в змінній,
# наприклад: а = 10
#   *  *  *  *  *  *  *  *  *  *  *  *   *
#   *                                    *
#   *                                    *
#   *                                    *
#   *                                    *
#   *                                    *
#   *                                    *
#   *                                    *
#   *                                    *
#   *  *  *  *  *  *  *  *  *  *  *  *   *
# -----------------------------------------
# rows = 10
# # first_line = last_line = ('* ' * rows)[:-1]
# # print(first_line)
# # for r in range(rows - 2):
# #     print('{0}{1}{0}'.format('*', ' ' * ((rows - 2) * 2 + 1)))
# # print(last_line)
# -------------------------------------------------------
# rows = 10
# first_line = last_line = ('* ' * rows)[:-1]
# print(first_line)
# for r in range(rows - 2):
#     print('*' + ' ' * ((rows - 2) * 2 + 1) + '*')
# print(last_line)
# --------------------------------------------------------
# a = 10
# i = a
# while i >= 1:
#     if i == a or i == 1:
#         j = a
#         while j > 0:
#             print('*  ', end='')
#             j -= 1
#         print(' ')
#     else:
#         j = a - 2
#         print('* ', end='')
#         while j > 0:
#             print('  ', end='')
#             j -= 1
#         print('         *')
#     i -= 1

# ----------------------------------------------------------
# -----------------------------------------------------
# Task 5*
# n = 10
# const = n
# while n != 0:
#     m = const
#     print("")
#     while m != 0:
#         if m == const or m == 1 or n == const or n == 1 or m == n or m == const - n + 1:
#             print("*  ", end="")
#         else:
#             print("   ", end="")
#         m -= 1
#     n -= 1
# --------------------------------------------------------
# n = 11
# const = n
# while n != 0:
#     m = const
#     print("")
#     while m != 0:
#         if m == const or m == 1 or n == const or n == 1 or m == n and m <= const / 2  \
#                 or m == const - n + 1 and n > const / 2:
#             print("*  ", end="")
#         else:
#             print("   ", end="")
#         m -= 1
#     n -= 1
# Task 5*
# rows = 10
# first_line = last_line = ('* ' * rows)[:-1]
# print(first_line)
# for r in range(rows - 2):
#     print('{0}{1}{0}'.format('*', ' ' * ((rows - 2) * 2 + 1)), )
# print(last_line)
# Task 6
# 6) Написати прогу яка перевіряє, чи ділиться одне число на друге
# num1 = 10
# num2 = 5
# if num1 % num2 == 0:
#     print('OK. Divides one number by another')
# else:
#     print('NO. One number is not divisible by another')
# ---------------------------------------------------------
# Task 7
# 7) в якій чверті знаходиться стрілка хв,
#   наприклад: ст = 12 - перша; ст = 34 - третя і т.д.
# minute = 65
# if minute >= 0 and minute < 15:
#     print('1 quarter')
# elif minute >= 15 and minute < 30:
#     print('2 quarter')
# elif minute >= 30 and minute < 45:
#     print('3 quarter')
# elif minute >= 45 and minute < 60:
#     print('4 quarter')
# else:
#     print('minute has 60 seconds')
# ------------------------------------------------------------
# Task 8
# 8) вивести табличку множення через while,
#    1   2   3   4   5   6   7   8   9
#    2   4   6   8  10  12  14  16  18
#    3   6   9  12  15  18  21  24  27
#    4   8  12  16  20  24  28  32  36
#    5  10  15  20  25  30  35  40  45
#    6  12  18  24  30  36  42  48  54
#    7  14  21  28  35  42  49  56  63
#    8  16  24  32  40  48  56  64  72
#    9  18  27  36  45  54  63  72  81
# n = 1
# while n != 10:
#     m = 1
#     while m != 10:
#         if n * m:
#             print(n * m, end=' ')
#             if len(str(n * m)) == 1:
#                 print(end=' ')
#         m += 1
#     print(end='\n')
#     n += 1
# ---------------------------------------------------------
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         res = i * j
#         if res // 10:
#             print(res, end=' ')
#         else:
#             print(res, end='  ')
#         j += 1
#     print()
#     i += 1
# ----------------------------------------------------------
# Task 9
# 9) вивести послідовність Фібоначі, кількість вказана в змінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
# fib1 = fib2 = 1
#
# n = int(input())
#
# if n < 2:
#     quit()
#
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# ---------------------------------------------------------
# a = 10
# fib1 = fib2 = 1
# print(fib1, fib2, end=' ')
# while a - 2 > 0:
#     sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = sum
#     print(fib2, end=' ')
#     a -= 1
# ----------------------------------------------------------
# Task 10
# 10) порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
# num = 548997777777
# str_num = str(num)
# i = 0
# list1 = []
# list2 = []
# for i in range(len(str_num)):
#     if int(str_num[i]) % 2 == 0:
#         list1.append(str_num[i])
#     else:
#         list2.append(str_num[i])
# print(len(list1))
# print(len(list2))
# print(list2)
# --------------------------
# num = 5489977
# str_num = str(num)
# i = 0
# even_number = 0
# odd_number = 0
# for i in range(len(str_num)):
#     if int(str_num[i]) % 2 == 0:
#         even_number += 1
#     else:
#         odd_number += 1
# print(even_number)
# print(odd_number)
# -----------------
# a = 54897
# even = 0
# odd = 0
# while a:
#     if a % 10 % 2:
#         odd += 1
#     else:
#         even += 1
#     a //= 10
# print(even)
# print(odd)

