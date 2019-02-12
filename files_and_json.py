
# Стандартный способ чтение файла
def read_file(filename):
    try:
        f = open(filename)
        content = f.read()
        # f.close
        return content
    finally:
        f.close

print(read_file('test.txt'))

# Альтернативный способ через контекстный менеджер
def way_file(filename):
    with open(filename) as f:
        return f.read()

    print(way_file('test.txt'))