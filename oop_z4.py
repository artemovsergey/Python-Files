'''
Создать класс Корзина, у которого можно вставить разную вместительность для разных объектов. В класс можно помещать
объекты. Создать класс Пакет, в который также можно помещать предметы. У него тоже есть вместимость
Создать класс, объекты которого можно помещать в корзину и пакет
Если  вместимости недостаточно сказать, что объект поместить нельзя

'''

class Corsina:

    def __init__(self,x):
        self.x = x
        self.count = []

    def add_element(self,element):
        
        # print('Вместительность корзины: {}'.format(self.x))
        
        if len(self.count) == 0:
            self.summa = 0
        
        if (element.kg > self.x):
            print('Товар не поместиться в корзину!')
        elif self.x != self.summa:
            self.count.append(element)
            self.summa += element.kg
            print('Можно добавить: {} кг'.format(self.x - (self.summa)) )   
        else:
            print('Вместимость максимальная!')
        
        # print('Cейчас в корзине: {}'.format(self.count))

class Packet(Corsina):
    pass


class Product(object):
    def __init__(self,name,kg):
        self.name = name
        self.kg = kg



korsina = Corsina(5)
korsina.add_element(Product('Молоко',1.5))
korsina.add_element(Product('Молоко',2.5))
korsina.add_element(Product('Молоко',1))
korsina.add_element(Product('Молоко',0.1))

paket = Packet(3)
print('Вместительность пакета: {}'.format(paket.x))
paket.add_element(Product('Сыр',3.0))


