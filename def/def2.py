def max_min(*args):
    try:
        print('Максимальный элемент: {}'.format(max(args)))
        print('Минимальный элемент: {}'.format(min(args)))
    except TypeError:
        print('Аргументы должны быть только числа')
    except ValueError:
        print('Аргумент должен быть минимум 1')

max_min()