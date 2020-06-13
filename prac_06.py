# 1) написати декоратор який обробляє функцію і виводить на
# початку роботи функції - "Start", в кінці роботи - "The end"
# def decor(func):
#     def wrap():
#         print('Start')
#         func()
#         print('The end')
#     return wrap
# @decor
# def some():
#     print('Hello my freund!!!!!!!!!')
# some()

# 2)  функція: def pr(): return 'Hello_boss_!!!'
#       написати декоратор який замінює нижні підчеркування
# на пробіли і повертає це значення
# def decor(func):
#     def wrap():
#         new_st = ' '.join(func().split('_')) ///// OR return func().replace('_', ' ')
#         return new_st
#     return wrap
# @decor
# def pr():
#     return 'Hello_boss_!!!'
# x = pr()
# print(x)

# 3) написать функцию на замыкание которая принимает лист,
# и при каждом вызове get() возвращает по одному значению этого листа,
# а если в листе не остается элементов то возвращает 'end'
some_list = [1, 2, 3, 4]

def closure(arr):
    count = 0
    def get_item():
        nonlocal count
        result = 'end' if count >= len(arr) else arr[count]
        count += 1
        return result
    return get_item

get = closure(some_list)
print(get())
print(get())
print(get())
print(get())
print(get())
print(get())
print(get())
