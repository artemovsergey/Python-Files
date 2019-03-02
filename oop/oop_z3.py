'''
*ЗАДАЧА 3:
Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)

'''
class Animal:
    pass

    def __init__(self,name,status_human):
        self.name = name
        self.status_human = status_human

class Human:

    def is_dangerous(self,animal):
        if animal.status_human:
            print('Данный зверь {} опасный для человека!'.format(animal.name))
        else:
            print('Это же {}. Это добрый зверь!'.format(animal.name))



tigr = Animal('Тигр',True)
rabbit = Animal('Кролик',False)

human1 = Human()
human1.is_dangerous(tigr)
human1.is_dangerous(rabbit)