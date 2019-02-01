# # Использование встроенное библиотеки для скрапинга

# from urllib.request import urlopen
# # html = urlopen("http://pythonscraping.com/pages/page1.html")  
# html = urlopen("http://stvcc.ru/")

# # print(html.read())



# #  Теперь воспользуемся другой библиотекой

# from bs4 import BeautifulSoup
# bsObj = BeautifulSoup(html.read())
# print( bsObj.title )

# Теперь хорошо напишем наш скрапер

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    
    #1
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    #2
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title

    
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print('Заголовок не найден')
else:
    print(title)