def sum_all(*numbers):
    summa = 0
    for i in numbers:
        summa+=i
    return summa
    
result = sum_all()
print(result)

def any_keywords(**numbers):
    print(numbers)


any_keywords(a=2,b=3,c=4)

def any_args(*numbers):
    print(numbers)


any_args(1,2,3,4)