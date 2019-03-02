
# Ввод переменных

# a = input("Введите a: ")
# b = input("Введите b: ")
# print(int(a)+int(b))



# Условные операторы

# name = "Лето"
# if name == "Лето":
#     print("Это правильный ответ")
# else:
#     print("Это не правильный ответ")



# Интервалы

# vvod = input('Введите мощность массива: ')
# massiv = range(int(vvod))

# print('Длина массива: ' + str(len(massiv)))

# print(list(massiv))



# Обход списка

# for elem in massiv:
#     print(str(elem)+" элемент")


# Повтореине цикла заданное количество раз

# input = int(input('Введите число: '))
# for elem in range(input):
#     print('Hello!')



# Создание собственных функций

# def say_hello():
#     ''' Описание функции '''
    # print ('Hello! '+ str(input('Введите имя: ')))
    # return 10 

# say_hello() 

# Вызов документации на определенную функцию

# print(input.__doc__)
# print(say_hello.__doc__)


# Использование модулей

# import random

# print(random.randint(0,10))


# for elem in range(10):
#     print(random.randint(5,10))

# import math
# print(round(math.sin(3),3))


# from math import sqrt
# print(sqrt(4))

# from math import * # импортирование всех функций

# print(cos(3))
# print(pi)

# from math import sqrt as mysqrt # новое имя

# print(mysqrt(9))


# Обработка исключений
# try:
#     print(7/0)
# except:
#     print('Деление на ноль!')
# finally:
#     print('Этот код выполнится в любом случае!')

# Работа с файлами
file = open(__file__+'test.txt','w')
file.write('Добавление текста в файл')
# print(file.read())  # только для режима 'r'

file.close()

# Техника среза списков
digits = [1,2,3,4,5]
print( digits[4:2:-1] )

#  начала среза, конец среза, шаг среза
# for elem in range(1,10)[1::2]:
# print( str(elem))


