user_input = int(input('Введите число: '))

for elem in range(2,user_input):
    if user_input % elem == 0:
        print('Обычное число!')
        # print('{} - делитель числа'.format(elem))
        break
    if elem == user_input-1:
        print('Это простое число!')
    
 # все кратные 5   

user_input1 = int(input('Введите первое число: '))
user_input2 = int(input('Введите второе число: '))

for elem in range(user_input1+1,user_input2):
    if elem % 5 == 0:
        print('Между числами {} и {} есть числа, кратные 5'.format(user_input1,user_input2))
        break
    if elem == user_input2-1:
        print('Между числами {} и {} нет чисел, кратных 5'.format(user_input1,user_input2))


