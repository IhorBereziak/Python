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

class Files:
    def swap(self):
        with open('file1.txt') as file1, open('file2.txt') as file2:
            file1, file2 = file2, file1
            f1 = file1.read().splitlines()
            f2 = file2.read().splitlines()
        return f'file1: {f1}, file2: {f2}'
    def to_dict(self):
        with open('file1.txt') as file1, open('file2.txt') as file2:
            l1 = [row for row in file1.read().splitlines()]
            l2 = [row for row in file2.read().splitlines()]
            d1 = dict(zip(l1, l2))
            d2 = dict(zip(l2, l1))
        return f'dict1: {d1}; dict2: {d2}'
f = Files().swap()
print(f)
dic = Files().to_dict()
print(dic)
def readlines():
    with open('file1.txt') as file1, open('file2.txt') as file2:
        # l1 = [row.rstrip('\n') for row in file1]
        # l2 = [row.rstrip('\n') for row in file2]
        l1 = list(map(lambda row: row.rstrip('\n'), file1))
        l2 = list(map(lambda row: row.rstrip('\n'), file2))
        print(l1)
        print(l2)
readlines()



