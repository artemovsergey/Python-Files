from urllib.request import urlopen
from  bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

# nameList =  bsOj.findAll("span",{"class":"green"})
# for elem in nameList:
#     print( elem.get_text() )


#  bsObj.tagName - получить первое вхождение тега на странице
#  bsObj.findAll(tagName,tagAttributes)  - получить список всех тегов на стрнице
#  elem.get_tesxt()  -  вывод контента, всегда надо делать в последнюю очередь

'''
findAll(tag, attributes,recursive,text,limit,keywords)   - > cписок
find(tag, attributes,recursive,text,keywords)  -> список
'''

print( bsObj.find("span",{"class":"red"} ))