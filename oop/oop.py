class Car:

    # All attributes
    # name = 'Kotlin'
    engine = 'V8'
    price = 1_000_000
    speed = 150
    # __test = True

    # Конструктор
    def __init__(self,name,engine,price):
        # print("Мащина {} создана хозяин!".format(self))
        self._name = name  # _ приватный атрибут (инкапсуляция) 
        self.engine = engine
        self.price = price
        self.test = True

    # Метод
    def move(self):
        '''
        Метод move
        '''
        # идентификатор текущего объекта
        print(self)
        # доступ к свойствам объекта
        self.name = 'Javascript'
        self.speed = 100
        # speed = 200

        # По умолчанию инстансные переменные наследуются от одноименных классовых переменных
        self.test = not self.test


car = Car('BMV','V8',1_500_500)

print(car.name)
print(car.test)

