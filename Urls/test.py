# # [{"name": "Felix Maina", "years": 21, "school": "Makerere"}]import json
# # # Data to be written
# # details = [{
# #         "name": "Felix Maina",
# #         "years": 21,
# #         "school": "Makerere"
# # }]
# # # Serializing JSON and writing JSON file
# # with open("data.json", "w") as file_object:
# #     json.dump(details, file_object)  # {"

# # wf=open('Urls/Url.txt',"r+")
# # lines=wf.readlines()
# # for i in lines:
# #     print(i.rstrip())

# # importing the csv module
# # import csv
	
# # # my data rows as dictionary objects
# # mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
# # 		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
# # 		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
# # 		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
# # 		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
# # 		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
	
# # # field names
# # fields = ['name', 'branch', 'year', 'cgpa']
	
# # # name of csv file
# # filename = "Csv/data.csv"
	
# # # writing to csv file
# # with open(filename, 'w') as csvfile:
# # 	# creating a csv dict writer object
# # 	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
# # 	# writing headers (field names)
# # 	writer.writeheader()
		
# # 	# writing data rows
# # 	writer.writerows(mydict)


# from lxml import html
# from bs4 import BeautifulSoup
# import requests
# import numpy as np
# import time
# import requests

# # wf=open('Urls/Url.txt',"r+")
# # lines=wf.readlines()
# # for i in lines:
# #     print(i.rstrip())

# def get_wine_links():
#     urlLinks=[]
#     wf=open('Urls/Url.txt',"r+")
#     lines=wf.readlines()
#     for i in lines:
#         urlLinks.append(i.rstrip())
#     return urlLinks


# def get_wine_info():
#     products=[]


#     links=get_wine_links()
#     # for i in links:
#     #         URL = f'{i}'
#     #         print(URL)
#     #         r = requests.get(URL)
#     #         soup=BeautifulSoup(r.content,'html5lib')
#     for i in range(0,len(links)):
#         URL = f"{links[i]}"
#         # print(URL)
#         r = requests.get(URL)
#         soup=BeautifulSoup(r.content,'html5lib')
#         # print(soup.prettify())
#         # print('***')
#         image=soup.find('img', {"id": "product-main-image"})
#         srcImg=image.attrs['src']
#         # print(srcImg)

        

#         desc=soup.find('div', {"id": "product-description"})

#         title=desc.find('h1').text
#         # print(title)

#         price=desc.find('span',{"class": "product-price"}).text
#         # print(price)

#         itemInfo=desc.find('div', {"id": "item-info"})
#         ulInfo=desc.find('ul')

#         # # print(itemInfo.prettify())
#         list=[]
#         for j in ulInfo.find_all('li'):
#             p=j.find('p')
#             # print(p.text)
#             if (p.text in ['Type:',"Country:","Bottle Size:",'Region:',"ABV:",'Grape:']):
#                 # print(p.text)
#                 # print(i.find_all('p')[1].text)s
#                 # print(i.find_all('p'))
#                 list.append(j.find_all('p')[1].text)
#         # print(len(list))

#         if(len(list)==6):
#             # print(len(list))
#             type, grape, country,region,abv,bottleSize = [i for i in list]
#         # print(type, grape, country,region,abv,bottleSize)

#         description=soup.find("div",{"class": "meta--text"}).text.strip()
#         # print(description)
#         keys=['id','image','title','price','type','grape','country','region','abv','bottlesize']
#         values=[i,srcImg,title,price,type,grape,country,region,abv,bottleSize]
#         # print([1,srcImg,title,price,type,grape,country,region,abv,bottleSize])
#         product={}
#         for k in range(0,len(keys)):
#             product[keys[k]]=values[k]
#         products.append(product)
#         time.sleep(2)
#         print(product)
#     # print(products)
#     return products

# def scraped_data_into_csv():
#     pass


import csv
import json


# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
	
# 	# create a dictionary
# 	data = {}
	
# 	# Open a csv reader called DictReader
# 	with open(csvFilePath, encoding='utf-8') as csvf:
# 		csvReader = csv.DictReader(csvf)
		
# 		# Convert each row into a dictionary
# 		# and add it to data
# 		for rows in csvReader:
			
# 			# Assuming a column named 'No' to
# 			# be the primary key
# 			key = rows['No']
# 			data[key] = rows

# 	# Open a json writer, and use the json.dumps()
# 	# function to dump data
# 	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
# 		jsonf.write(json.dumps(data, indent=4))


# # Call the make_json function
# make_json("products-data.csv", )
data=[]
with open("products-data.csv", encoding='utf-8') as csvf:
	csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
	for rows in csvReader:
            data.append(rows)
			
			# Assuming a column named 'No' to
			# be the primary key
			

	# Open a json writer, and use the json.dumps()
	# function to dump data
with open("products-data.json", 'w', encoding='utf-8') as jsonf:
	jsonf.write(json.dumps(data, indent=4))





    



            

  



    

# get_wine_info()

    
    






