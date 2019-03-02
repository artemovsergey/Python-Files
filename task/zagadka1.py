print('Загадка 1. Не лает, не кусает - в дом не пускает!')


input_user = None
while input_user != 'Собака':
    input_user = input('Ответ: ')
    if input_user == 'Собака':
        print('Это правильный ответ!')
    else:
        print('Ответ неправильный!')