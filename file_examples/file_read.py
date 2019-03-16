with open('example.txt',encoding = 'cp1251') as file:
	# content_only_five_chars = file.read(5)
	# content_all = file.read()
	for line in file:
		print(line.strip() + ":" + str(len(line.strip())))