import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.ah.nl"

page = requests.get(URL+"/producten")

soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find_all("div", class_="product-category-overview_category__vqzcb")

product_types = []

for result in results:
    info = result.find("a", class_="taxonomy-card_imageLink__4b6bk")
    type = info['title']
    link = info['href']
    product_types.append({'Type': type, 'link':link})



page = requests.get(URL+product_types[0]['link'])
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("article", class_="product-card-portrait_root__ZiRpZ product-grid-lane_gridItems__BBa4h")

products = []

for result in results:
    info = result.find("a", class_="link_root__EqRHd")
    name = info['title']
    link = info['href']
    products.append({'name': name, 'link':link})



driver = webdriver.Chrome()
driver.get(URL+products[4]['link'])


cookie_button = driver.find_element(By.XPATH, '//*[@id="accept-cookies"]')

cookie_button.click()

time.sleep(1)

table = driver.find_element(By.XPATH,'//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table')

body = table.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody')

rows = body.find_elements(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr')

nutrition = []

for index, row in enumerate(rows):
    name = body.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr['+str(index+1)+']/td[1]').text
    macro = body.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr['+str(index+1)+']/td[1]').text
    nutrition.append({"name": name, "macro":macro})


print(nutrition)