slovo = input('Загадайте слово: ')
print('_____________________________')

i = 0 
j = 0
arr = []
l = len(slovo)

while j < l:
    arr.append('*')
    j+=1

print('Итак, в слове {} букв: '.format(len(slovo)))

while i < 5:
    print(arr)
    bukva = input('Введите букву: ')


    if bukva in slovo:
        # найти индекс буквы fuction

        for index in range(0,l):
            if [*slovo][index] == bukva:
                arr.__delitem__(index)
                arr.insert(index,bukva)


        if arr == [*slovo]:
            print(arr)
            print('_____________________________')
            print('Поздравляем вы угадали слово!')
            print('_____________________________')
            break
    else:
        print('Нет такой буквы!')
        print()
        i+=1
        if i == 5:
            print('Ваши попытки закончились')
        else:
            print('У вас осталось {} попыток'.format(5-i))
        
print()
# print('Угадано букв: {}'.format(arr))
print('Было загадано слово: {}'.format(slovo))

