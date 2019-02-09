def sum_all(*numbers)
    summa = 0
    for i in numbers do
        summa+=i
    end
    return summa
end

result = sum_all(1,2,3)
print(result)
puts

def return_hash(**hash)
    p hash
end

return_hash(a:2,b:3,c:4,d:5)