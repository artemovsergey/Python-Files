

def test(t,*params,**dictions):
	'''
	*params  - все позиционные параметры оформляет в массив,
	начиная с этой позиции

	**dictions - все ключевые параметры оформляет в словарь, начиная с этой
	позиции

	'''
	summa = 0
	for i in params:
		summa+=i

	print(summa)
	print(dictions)
	print(params)

# test(1,2,3,4,d = 5,c = 7)


def test2(a,*,b,c):
	'''
	* - начиная с позиции после звездочки все аргументы вызываются
	только по ключу

	'''
	print("Hello")
	
	# print(params)

test2(1,b = 2,c = 3)






