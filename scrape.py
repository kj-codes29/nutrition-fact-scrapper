import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.ah.nl"
driver = webdriver.Chrome()

driver.get(URL+"/producten")

cookie_button = driver.find_element(By.XPATH, '//*[@id="accept-cookies"]')

cookie_button.click()

time.sleep(1)

results = driver.find_elements(By.CLASS_NAME, 'product-category-overview_category__vqzcb')

product_types = []

for result in results:
    info = result.find_element(By.CLASS_NAME, 'taxonomy-card_imageLink__4b6bk')
    img_element = result.find_element(By.CLASS_NAME, 'taxonomy-card_image__RPcqB')
    type = info.get_attribute('title')
    link = info.get_attribute('href')
    img_link = img_element.get_attribute('src')
    product_types.append({'Type': type, 'link':link, 'Img': img_link})

print(product_types)

'''
page = requests.get(URL+product_types[0]['link'])
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("article", class_="product-card-portrait_root__ZiRpZ product-grid-lane_gridItems__BBa4h")

products = []

for result in results:
    info = result.find("a", class_="link_root__EqRHd")
    name = info['title']
    link = info['href']
    products.append({'name': name, 'link':link})


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
'''