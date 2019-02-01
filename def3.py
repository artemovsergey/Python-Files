def even_odd(*args,flag = True):
    
    arr_even = []
    arr_odd = []
    for i in args:
        if i % 2 == 0:
            arr_even.append(i)
        else:
            arr_odd.append(i)
        
    if flag ==  False:
        return arr_odd
    return arr_even

result = even_odd(1,2,3,4,5)
print(result)

result = even_odd(1,2,3,4,5,flag = False)
print(result)