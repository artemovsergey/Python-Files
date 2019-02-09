'''
ЗАДАЧА 1:
Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
Также у него должен быть следующий набор методов: know(person), который позволяет 
добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека

'''

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    def know(self,new_friend):

        '''
        Добавляет человека в список знакомых
        '''

        self.friends.append(new_friend.name)
        return self.friends

    def is_know(self,user):
        '''
        Знакомы ли два человека
        '''
        if user.name in self.friends:
            print('Я знаком с {}'.format(user.name))
        else:
            print('Я не знаком с {}'.format(user.name))


user = Person('Vasia',20)
print('У пользовтеля {} друзей'.format(len(user.friends)))

user1 = Person('Petya',30)

user.is_know(user1)

print('--------------------------------------------------')

user.know(user1)

print('У пользовтеля {} друзей'.format(len(user.friends)))
user.is_know(user1)

