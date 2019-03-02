from random import randint
print('Загадано случайное число 0 до 10: ')
user_input = randint(0,10)

input_user = input('Введите число: ')
while input_user != user_input:

    while input_user == ' ' or input_user == '':
        input_user = input('Введите число: ')

    if int(input_user) > user_input:
        input_user = int(input('Надо меньше!: '))
    else:
        input_user = int(input('Надо больше!: '))

print('Поздравляем вы угадали число! Было загадано число {}'.format(user_input))