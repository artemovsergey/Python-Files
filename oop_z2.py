'''
*ЗАДАЧА 2:
Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

'''

class Printer:
    def log(self,*elem):
        print([*elem])

class FormattedPrinter(Printer):

    def log(self,*elem):

        print('*'+('*'*(len(str([*elem]))-2))+'*')
        print([*elem])
        print('*'+('*'*(len(str([*elem]))-2))+'*')



a = Printer()
a.log(1,2,3,4,5)
a.log('Текст')

print('---------------')

b = FormattedPrinter()
b.log(1,2,3,4,5)

print('---------------')
b.log('Текст')

