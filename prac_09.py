# 1) -cоздать два файла:
# file1.txt:
# John
# 32
# BMW
#
# file2.txt:
# name
# age
# car
#
# -создать класс Files, который будет принимать два файла
# - в этом классе должен быть метод "swap", который будет менять содержимое этих двух файлов между собой
# - в этом классе должен быть метод "to_dict", который будет возвращать словарь созданный из этих
# двух файлов (используем функцию "zip" в комбинации с функцией "dict")
# пример:
# {'name': 'John', 'age': 32, 'car': 'BMW'}
# {'John': 'name', 32: 'age', 'BMW': 'car'}
#
# - для чтения из файла используем функцию файла "readlines" (возвращает лист строк файла)
# - для удаление "\n" используем функцию "map"

# class Files:
#     def swap(self):
#         with open('file1.txt') as file1, open('file2.txt') as file2:
#             file1, file2 = file2, file1
#             f1 = file1.read().splitlines()
#             f2 = file2.read().splitlines()
#         return f'file1: {f1}, file2: {f2}'
#     def to_dict(self):
#         with open('file1.txt') as file1, open('file2.txt') as file2:
#             l1 = [row for row in file1.read().splitlines()]
#             l2 = [row for row in file2.read().splitlines()]
#             d = dict(zip(l2, l1))
#         return d
# f = Files().swap()
# print(f)
# dic = Files().to_dict()
# print(dic)
# def readlines():
#     with open('file1.txt') as file1, open('file2.txt') as file2:
#         # l1 = [row.rstrip('\n') for row in file1]
#         # l2 = [row.rstrip('\n') for row in file2]
#         l1 = list(map(lambda row: row.rstrip('\n'), file1))
#         l2 = list(map(lambda row: row.rstrip('\n'), file2))
#         print(l1)
#         print(l2)
# readlines()

# 0) створити клас User, який в init приймає name i mail.
# 1) створити клас Letter, який в init приймає text
# 2) створити функцію send_letter яка створює об'єкт user і letter,
# 3) створює файл (назва файла має виглядати так "{user.name}.txt" де user.name - це імя щойно створеного юзера),
# 4) текст файла має записатися з об'єкта letter.text
# 5) має бути глобальний словник users де ключами є об'єкт user а значенням об'єкт letter,
# 6) добавлення в словник має відбуватися автоматично коли викликається функція send_letter
# 7) зробити меню для цього всього:
#   1) надіслати листа - send_letter
#   2) переглянути всіх юзерів з словника - вивести список імен які є в словнику
#   3) переглянути лист - запитати ім'я, якщо є в словнику вивести лист, якщо немає то сказати що немає такого
#   4) вихід


class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

class Letter:
    def __init__(self, text):
        self.text = text

users = {}

def send_letter(name, mail, text):
    user = User(name, mail)
    letter = Letter(text)
    with open(f"{user.name}.txt", 'w') as file:
        file.write(letter.text)
    users[user.name] = {f'{user.mail}': letter.text}

def hr():
    print('------------------------------------------------------')

while True:
    print('1. Run send_letter')
    print('2. Show all users; list name what is in dict')
    print('3. Search name')
    print('4. Exit')
    choice = input('Make your choice: ')
    print('')
    if not choice.isdigit():
        continue
    choice = int(choice)
    if choice == 1:
        name = input('Enter name: ')
        mail = input('Enter e-mail: ')
        text = input('Enter text: ')
        send_letter(name, mail, text)
    if choice == 2:
        hr()
        for item in users:
            print(item)
        hr()
    if choice == 3:
        name = input('Enter name: ')
        if name not in users:
            print('This name is not in file')
        else:
            for k, v in users.items():
                print(f'{k}: {v}')
    if choice == 4:
        break