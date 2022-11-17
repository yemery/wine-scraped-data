from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import requests

# wf=open('Urls/Url.txt',"r+")
# lines=wf.readlines()
# for i in lines:
#     print(i.rstrip())

def urlFile():
    urlLinks=[]
    wf=open('Urls/Url.txt',"r+")
    lines=wf.readlines()
    for i in lines:
        urlLinks.append(i.rstrip())
    return urlLinks

def getPost():
    # links=urlFile()
    # for i in links:
    #         URL = f'{i}'
    #         print(URL)
    #         r = requests.get(URL)
    #         soup=BeautifulSoup(r.content,'html5lib')
    URL = "https://www.thegoodwineshop.co.uk/products/stoneweaver-pinot-noir"
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    # print(soup.prettify())
    image=soup.find('img', {"id": "product-main-image"})
    srcImg=image.attrs['src']
    # print(srcImg)

    desc=soup.find('div', {"id": "product-description"})

    title=desc.find('h1').text
    # print(title)

    price=desc.find('span',{"class": "product-price"}).text
    # print(price)

    # itemInfo=desc.find('div', {"id": "item-info"})
    ulInfo=desc.find('ul')

    # print(itemInfo.prettify())
    list=[]
    for i in ulInfo.find_all('li'):
        p=i.find('p')
        # print(p.text)
        if (p.text in ['Type:',"Country:","Bottle Size:",'Region:',"ABV:",'Grape:']):
            # print(p.text)
            # print(i.find_all('p')[1].text)s
            # print(i.find_all('p'))
            list.append(i.find_all('p')[1].text)
    # print(list)

    type, grape, country,region,abv,bottleSize = [i for i in list]
    # print(type, grape, country,region,abv,bottleSize)

    description=soup.find("div",{"class": "meta--text"}).text.strip()
    # print(description)



            

  



    

getPost()
    
    






