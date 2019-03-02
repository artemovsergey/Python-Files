from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# for link in bsObj.findAll("a"):  # вывести все ссылки с тегом  <a>
#     if 'href' in link.attrs:
#         print( link.attrs['href'] )
#     print('----------------')

random.seed(datetime.datetime.now()) # начальное значение для генератора случайных чисел

def getLinks(articleUrl):
    html =  urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj =  BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

#  Вывод инфомрации
s = 0
while len(links) > 0 and s != 10:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    s += 1
    links = getLinks(newArticle)
print ('Выведено ссылок: ' + str(s))


