# Решение квадратного уравнения ax2+bx+c

from math import sqrt

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))


def Disk(a,b,c):

    '''Решение квадратного уравнения'''

    d = b*b-4*a*c
    if d>0:
        
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        print('Уравнение имеет два корня: ' + str(round(x1,3)) + ' и ' + str(round(x2,3)))
    elif d == 0:
        print('Уравнение имеет один корень: ' + str(round(x,3)))
        x = (-b)/(2*a)
    else:
        print('Корней нет')


Disk(a,b,c)