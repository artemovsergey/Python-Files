class Car:

    def __init__(self):
        self.age = 15

    def test(self):
        print('Вызван метод родителя')
        self.name = "Вася"

class Lorry(Car): 
    
    @staticmethod
    def count():
        return '123'

    def __init__(self,test):
        super().__init__()   # логика родительского класса
        print(str(self.age) + test)

 
# a = Car()
# a.test() 

b = Lorry('text')
# print ( Car.__mro__)

int(5) + int(10)
print( 5.+(5) )