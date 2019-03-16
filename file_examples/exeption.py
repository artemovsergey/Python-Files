try: # просто код - обычный код
	x = 0
	a = 1/x
except ZeroDivisionError as e: # если что ошибка
	print("На ноль делить нельзя! :  {}". format(e) )
	# raise ZeroDivisionError
else: 
	print("Вот видишь! Все прошло просто отлично!")
finally:
	print("Проверка завершена! ...")