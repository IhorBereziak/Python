# 1) створити клас Letter, зі змінною __count.
# 2) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 3) при створені об'єкта __count має збільшуватися на 1
# 4) має бути метод який створює текстовий файл і записує туди текст(__text) даного об'єкта
# 5) має бути метод(метод класу) для виводу __сount
class Letter:
    __count = 0
    def __init__(self):
        self.__text = ''
        Letter.__count += 1
    @property
    def my_text(self):
        return self.__text
    @my_text.setter
    def my_text(self, text):
        self.__text = text

    def new_file(self):
        with open('file3.txt', 'a') as file:
            file.write(self.__text + '\n')
    @classmethod
    def init(cls):
        print(f'count: {cls.__count}')

letter = Letter()
letter.my_text = 'Hello world!'
print(letter.my_text)
letter.new_file()
letter.my_text = 'Hello Ukraine!'
letter.new_file()
letter2 = Letter()
Letter.init()


