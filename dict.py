def params(**dict):
	for key,value in dict.items():
		print(key,value)


params(a=3,b=4,c=5)
# Можно ли передать в функцию словарь?
hash_new = {"a":3,"b":3,"c":3}
params(**hash_new) # ** - распаковывает словарь по ключевым параметрам


# Также работает и со списком
def list_params(*list):
	for i in list:
		print(i,end = ' ')

list_params(1,2,3,4,5)
l = [1,2,3,4,5]
print()
list_params(*l)
	