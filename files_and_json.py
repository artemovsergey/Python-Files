
# Стандартный способ чтение файла
def read_file(filename):
    try:
        f = open(filename)
        content = f.read()
        # f.close
        return content
    finally:
        f.close

# Альтернативный способ через контекстный менеджер
def way_file(filename):
    with open(filename) as f:
        return f.read()

# Запись в файл
def write_to_file(filename):
    with open(filename,'a') as f:
        f.write('Новый текст в конце файла!')


if __name__ == '__main__':
    print(read_file('test.txt'))
    print(way_file('test.txt'))
    # Мы работаем с файлом, пока он есть
    write_to_file('test.txt') 