# Обработка исключений
try:
    1/0
except ValueError:
    print('Эта надпись будет выведена только для ValueError!')
except ZeroDivisionError as e:
    print("Ошибка {} была занесена в переменную e".format(e))
except TypeError:
    pass
else:
    print('Ошибки нет. Этот текст видно')
finally:
    print('++++++++++++++++++')

# raise TypeError
