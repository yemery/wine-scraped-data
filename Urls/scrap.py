from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)
webPath="https://www.thegoodwineshop.co.uk/"
driver.get(webPath)
time.sleep(5)
#Agree btn
driver.find_element(By.XPATH, "//*[@id='preview_img']/div[1]/section/div/div/div[1]/button").click()
time.sleep(5)


#navLink 
driver.find_element(By.XPATH, "//*[@id='main-nav']/li[1]/a").click()
time.sleep(5)
# /*[@id='sparq-container']/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div[2]

# driver.find_element(By.XPATH, "//*[@id='sparq-container']/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]").click()
# ParentDiv=driver.find_elements(By.CLASS_NAME,'sparq-result-inner')
# # linkChild=ParentDiv.find_element(By.TAG_NAME,'a').get_attribute("href")
# for i in ParentDiv:
#     p=i.find_element(By.TAG_NAME,'a').get_attribute('href')
#     print(p)
productList=[]
for i in range(0,2):
    ParentDiv=driver.find_elements(By.CLASS_NAME,'sparq-result-inner')
    for i in ParentDiv:
        product=i.find_element(By.TAG_NAME,'a').get_attribute('href')
        # productList.append(product)
        with open("Url.txt", "a") as f:
            f.write(f'{product}\n')
            
    
    # print(p)
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[@id='sparq-container']/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/ul/li[8]/button").click()
    time.sleep(10)
    # driver.find_element(By.XPATH,"/html/body/div[15]/div/div/div/div/div/div/button/svg/circle").click()

print(productList)
# print(linkChild)
time.sleep(5)
driver.quit()

