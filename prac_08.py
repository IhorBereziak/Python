# 1) створити модуль(файл) з функціями
#    def add_to_list(list,item):
#     list.append(item)
#     return len(list)
#
#   def create_list():
#     list =[]
#     return list
#
#   1) треба прямо в функції add_to_list дописати код який буде обробляти
#   помилку якщо передали не ліст і буде запускати іншу функцію
#   2) якщо ніякої помилки не було в глобальну змінну записати True в іншому випадку False
#   3) імпортнути add_to_list в якомусь іншому файлі, викликати метод add_to_list

error = None

def add_to_list(list, item):
    global error
    try:
        list.append(item)
        error = False
    except AttributeError:
        error = True
        list = create_list()
    finally:
        print('Error', error)
    return len(list)


def create_list():
    list = []
    return list
