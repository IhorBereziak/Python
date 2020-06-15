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
#     def __init__(self, file1, file2):
#         self.file1 = file1
#         self.file2 = file2
#         self.lists = []
#
#     def swap(self):
#         if self.lists:
#             self.lists.clear()
#         with open(self.file1) as file1, open(self.file2) as file2:
#             self.lists.append(file1.readlines())
#             self.lists.append(file2.readlines())
#         list1, list2 = self.lists
#         with open(self.file1, 'w') as file1, open(self.file2, 'w') as file2:
#             file1.write(''.join(list2))
#             file2.write(''.join(list1))
#
#     def to_dict(self):
#         if not self.lists:
#             with open(self.file1) as file1, open(self.file2) as file2:
#                 self.lists.append(file1.readlines())
#                 self.lists.append(file2.readlines())
#         list1, list2 = self.lists
#         list1 = list(
#             map(lambda item: int(item.rstrip('\n')) if item.rstrip('\n').isdigit() else item.rstrip('\n'), list1))
#         list2 = list(
#             map(lambda item: int(item.rstrip('\n')) if item.rstrip('\n').isdigit() else item.rstrip('\n'), list2))
#         return dict(zip(list1, list2))
#
# file = Files('file1.txt', 'file2.txt')
# file.swap()
# print(file.to_dict())
# -----------------------------------------------------------------------------------------------------------------
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


# class User:
#     def __init__(self, name, mail):
#         self.name = name
#         self.mail = mail
#
# class Letter:
#     def __init__(self, text):
#         self.text = text
#
# users = {}
#
# def send_letter(name, mail, text):
#     user = User(name, mail)
#     letter = Letter(text)
#     with open(f"{user.name}.txt", 'w') as file:
#         file.write(letter.text)
#     users[user.name] = {'email': user.mail, 'text': letter.text}
#
# def hr():
#     print('------------------------------------------------------')
#
# while True:
#     print('1. Run send_letter')
#     print('2. Show all users; list name what is in dict')
#     print('3. Search name')
#     print('4. Exit')
#     choice = input('Make your choice: ')
#     print('')
#     if not choice.isdigit():
#         continue
#     choice = int(choice)
#     if choice == 1:
#         name = input('Enter name: ')
#         mail = input('Enter e-mail: ')
#         text = input('Enter text: ')
#         send_letter(name, mail, text)
#     if choice == 2:
#         hr()
#         for item in users:
#             print(item)
#         hr()
#     if choice == 3:
#         name = input('Enter name: ')
#         hr()
#         if name not in users:
#             print('This name is not in file')
#         else:
#             for k, v in users.items():
#                 print(f'{k}: {v}')
#         hr()
#     if choice == 4:
#         break
#----------------------------------------------------------------------------
# list = [1, 2, 3, 4, 5]
#
# a,_, b, *_ = list
# print(a)
# print(b)