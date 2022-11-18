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

def get_wine_links():
    urlLinks=[]
    wf=open('Urls/Url.txt',"r+")
    lines=wf.readlines()
    for i in lines:
        urlLinks.append(i.rstrip())
    return urlLinks


def get_wine_info():
    products=[]


    links=get_wine_links()
    # for i in links:
    #         URL = f'{i}'
    #         print(URL)
    #         r = requests.get(URL)
    #         soup=BeautifulSoup(r.content,'html5lib')
    for i in range(0,len(links)):
        URL = f"{links[i]}"
        # print(URL)
        r = requests.get(URL)
        soup=BeautifulSoup(r.content,'html5lib')
        # print(soup.prettify())
        # print('***')
        image=soup.find('img', {"id": "product-main-image"})
        srcImg=image.attrs['src']
        # print(srcImg)

        

        desc=soup.find('div', {"id": "product-description"})

        title=desc.find('h1').text
        # print(title)

        price=desc.find('span',{"class": "product-price"}).text
        # print(price)

        itemInfo=desc.find('div', {"id": "item-info"})
        ulInfo=desc.find('ul')

        # # print(itemInfo.prettify())
        list=[]
        for j in ulInfo.find_all('li'):
            p=j.find('p')
            # print(p.text)
            if (p.text in ['Type:',"Country:","Bottle Size:",'Region:',"ABV:",'Grape:']):
                # print(p.text)
                # print(i.find_all('p')[1].text)s
                # print(i.find_all('p'))
                list.append(j.find_all('p')[1].text)
        # print(len(list))

        if(len(list)==6):
            # print(len(list))
            type, grape, country,region,abv,bottleSize = [i for i in list]
        # print(type, grape, country,region,abv,bottleSize)

        description=soup.find("div",{"class": "meta--text"}).text.strip()
        # print(description)
        keys=['id','image','title','price','type','grape','country','region','abv','bottlesize']
        values=[i,srcImg,title,price,type,grape,country,region,abv,bottleSize]
        # print([1,srcImg,title,price,type,grape,country,region,abv,bottleSize])
        product={}
        for k in range(0,len(keys)):
            product[keys[k]]=values[k]
        products.append(product)
        time.sleep(2)
        print(product)
    # print(products)
    return products

def scraped_data_into_csv():
    pass







    



            

  



    

get_wine_info()

    
    






