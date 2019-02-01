from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)

# Cбор данных из таблиц

# for child in bsObj.find("table",{"id":"giftList"}).descendants:
#     print(child)


# Работа с одноуровневыми элементами

# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

# Работа с родительскими элементами

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())




# Применение регулярных выражений

# import re
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for elem in images: 
#     print(elem['src'])

# Применение lambda выражений

# print(bsObj.findAll(lambda tag: len(tag.attrs) == 2))