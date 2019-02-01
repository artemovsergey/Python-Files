from urllib.request import urlopen
from  bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Метод извлекает список всех внутренних ссылок, найденных на странице
def getInternakLinks(bsObj,includeUrl):
    internalLinks = []
    #Находит все ссылки, которые начинаются с "/"
    for link in bsObj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    print("Сканирование завершено!")           
    return internalLinks
    

# Метод извлекает список всех внешних ссылок, найденных на странице
def getExternakLinks(bsObj,excludeUrl):
    externallinks = []
    # Находит все ссылки, которые начинаются с "http" или "www"
    # не содержат текущего URL - адреса
    for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    print("Сканирование завершено!") 
    return externallinks
    

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj =  BeautifulSoup(html)
    externallinks = getExternakLinks(bsObj,splitAddress(startingPage)[0])
    if len(externallinks) == 0:
        internallinks = getInternakLinks(bsObj,startingPage)
        return getExternakLinks(bsObj,internallinks[random.randint(0,len(internallinks)-1)])
    else:
        return externallinks[random.randint(0,len(externallinks)-1)]

def followExternalOnly(startingSite):
    externallink = getRandomExternalLink("http://oreilly.con")
    print("Random external link is ",externallink)
    followExternalOnly(externallink)

followExternalOnly("http://oreilly.con")


# html = urlopen("http://oreilly.com")
# bsObj =  BeautifulSoup(html)

# getInternakLinks(bsObj,splitAddress("http://oreilly.com")[0])