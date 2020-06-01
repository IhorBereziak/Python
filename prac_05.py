# 1) написати функцію, яка знаходить середнє значення вхідних аргументів
#   і повертає це значення. Цих вхідних аргументів може бути безліч
# average_number = lambda *args: sum(args)/len(args)
# print(average_number(5, 7, 8, 12))
# 2) написати програму для копірайтерів)
#   програма має робити:
#   - вивести загальну кількість слів з текста(всі слова які мають більше двох букв)
# string = 'Hello is my frend Petro'
# count_world = lambda str: len([word for word in str.split() if len(word) > 2])
# print(count_world(string))
#   - вивести кількість вказаного символу у тексті(
# string = 'Hello is my frend Petro'
# count_symbol = lambda str, sm: 'введено більше 1-го символу' if len(sm) > 1 else str.count(sm)
# print(count_symbol(string, 'p'))
#   - вивести число яке вказує скільки разів зустрічається в тексті введене слово
# string = 'hello hello hello Ihor Ihor'
# count_world = lambda str, world: str.count(world)
# print(count_world(string, 'hello'))
#   - вивести найчастіше використовуване слово в тексті(більше двох букв)
# string = 'hello hello hello Ihor Ihor'
# moda_world = lambda str: str.split()[[str.count(world) for world in str.split()].index(max([str.count(world) for world in str.split()]))]
# print(moda_world(string))
#   - це все через меню має бути:
#    - введіть текст
#    - загальна кількість слів у тексті
#    - символ у тексті(к-сть)
#    - слово у тексті (к-сть)
#    - найчастіше вживане слово
# -------------------------------------
# 3 написать lambda функцию которая принимает строку и
# возвращает лист слов, при этом каждое слово это лист его букв:
# к примеру:
# 'Hello from owu' => [['H', 'e', 'l', 'l', 'o'], ['f', 'r', 'o', 'm'], ['o', 'w', 'u']]
# string = 'Hello from owu'
# list_world = lambda str: [list(world) for world in str.split()]
# list_world1 = lambda str: [[ch for ch in world] for world in str.split()]
# print(list_world(string))
# print(list_world1(string))
# ----------------------------------------------------------------------------
# str = 'Some text in@ !!!!noteb@ook'
# count_words = lambda str, exclude_list:len([fword for fword in [''.join(ch for ch in word if ch not in exclude_list) for word in str.split()] if len(fword) > 2])
# print(count_words(str, [',', '!', '@']))