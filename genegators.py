# Нужно написать генератор, который каждый раз бы возвращал новое случайное число
s = (i for i in range(10)) # генератор
print(s) # инстанс генератора
print(next(s)) # работа генерации
print(list(s))  # превращение генератора в список

print(iter([1,2,3])) # превращение списка в генератор)


# Генератор это функция с ключевым словом yield

# Это обычная функция
def gen():
    iter = 0
    s = 10
    while iter < s:
        return iter
        iter+=1
    
print(gen())
print('------------')
# Это генератор 
def gen1():
    iter = 0
    s = 10
    while iter < s:
        yield iter
        iter+=1
    
generator = gen1()  
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
