
import random
# Моделируем поле 
x = [['*','*','*'],['*','*','*'],['*','*','*']]

print()

print('Игра "Крестики - нолики": ')
print()

def show_game():
    print()
    print(x[0][0],x[0][1],x[0][2])
    print(x[1][0],x[1][1],x[1][2])
    print(x[2][0],x[2][1],x[2][2])
    print()

def rules(x,symbol):
    # Выигрывает тот игрок, кто заполнит ячейки
    #  (x00 x01 x02) (x20 x21 x22) (x00 x10 x20) (x02 x12 x22) (x20 x11 x02) (x00 x11 x22)
    #  (x10 x11 x12) (x01 x11 x21)

    if ((x[0][0] == symbol) and (x[0][1] == symbol) and (x[0][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[2][0] == symbol) and (x[2][1] == symbol) and (x[2][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[0][0] == symbol) and (x[1][0] == symbol) and (x[2][0] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[0][2] == symbol) and (x[1][2] == symbol) and (x[2][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[2][0] == symbol) and (x[1][1] == symbol) and (x[0][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[0][0] == symbol) and (x[1][1] == symbol) and (x[2][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[1][0] == symbol) and (x[1][1] == symbol) and (x[1][2] == symbol)):
        print ('Победа игрока ' + symbol)
        return True
    if ((x[0][1] == symbol) and (x[1][1] == symbol) and (x[2][1] == symbol)):
        print ('Победа игрока ' + symbol)
        return True    
        
show_game()

all_choice = ['00','01','02','10','11','12','20','21','22']

while True:
    
    print('-------------------------------------')
    user_inputX = input('Введите координатe X: ')
    user_inputY = input('Введите координатe Y: ')

    x[int(user_inputX)].__delitem__(int(user_inputY))    
    x[int(user_inputX)].insert(int(user_inputY),'X')
    
    user_xy =user_inputX + user_inputY
    all_choice.remove(user_xy)
    
    print()
    print(all_choice)
    print('Ваш ход: {}'.format(user_xy))

    show_game()
    
    
    if rules(x,'X'):
        break

    if ('*' not in x[0]) and ('*' not in x[1]) and ('*' not in x[2]):
        print('Ничья!')
        break

    print('-----------------------------------------')


    # 2 Ход компьютера: рандомно выбирает не занятые ячейки и заполняет 'O'
    
    get_xy = random.choice(all_choice)
    get_x = int([*get_xy][0])
    get_y = int([*get_xy][1])
    

    x[get_x].__delitem__(get_y)
    x[get_x].insert(get_y,'O')
    all_choice.remove(get_xy)
    print(all_choice)
    print('Ход компьютера:{}'.format(get_xy))
    show_game()
    
    if rules(x,'O') or (('*' not in x[0]) and ('*' not in x[1]) and ('*' not in x[2])):
        break
    
    if ('*' not in x[0]) and ('*' not in x[1]) and ('*' not in x[2]):
        print('Ничья!')
