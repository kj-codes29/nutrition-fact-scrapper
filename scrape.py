from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.ah.nl"
driver = webdriver.Chrome()

driver.get(URL+"/producten")

cookie_button = driver.find_element(By.XPATH, '//*[@id="accept-cookies"]')

cookie_button.click()

driver.implicitly_wait(1)

categories = driver.find_elements(By.CLASS_NAME, 'product-category-overview_category__vqzcb')

product_types = []

for category in categories:
    info = category.find_element(By.CLASS_NAME, 'taxonomy-card_imageLink__4b6bk')
    img_element = category.find_element(By.CLASS_NAME, 'taxonomy-card_image__RPcqB')
    type = info.get_attribute('title')
    link = info.get_attribute('href')
    img = img_element.get_attribute('src')
    product_types.append({'Type': type, 'link':link, 'image': img})

categories[0].click()

driver.implicitly_wait(1)

product_list = []



def convert_table_info():
    table = driver.find_element(By.XPATH,'//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table')

    body = table.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody')

    rows = body.find_elements(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr')

    nutrition = []

    for index, row in enumerate(rows):
        name = body.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr['+str(index+1)+']/td[1]').text
        macro = body.find_element(By.XPATH, '//*[@id="start-of-content"]/div[2]/div/div[1]/div[1]/div[3]/table/tbody/tr['+str(index+1)+']/td[2]').text
        nutrition.append({"name": name, "macro":macro})
    
    return nutrition

def convert_product(product):
    info = product.find_element(By.CLASS_NAME, 'link_root__EqRHd')
    img_element = product.find_element(By.TAG_NAME, 'img')
    name = info.get_attribute('title')
    link = info.get_attribute('href')
    img = img_element.get_attribute('src')

    product.click()

    driver.implicitly_wait(1)

    # nutrition facts
    nutrition = convert_table_info()
    product_list.append({'name': name, 'link':link, 'image':img, 'Nutrition Info': nutrition})

    # go back in history
    driver.back()
    driver.implicitly_wait(1)
        

# print(nutrition)

def get_displayed_amount():
    total_products_info = driver.find_element(By.XPATH, '//*[@id="start-of-content"]/div[3]/span').text
    total_products_info = total_products_info.split()
    current = int(total_products_info[0])
    total= int(total_products_info[3])
    return current, total

current_amount, total_amount = get_displayed_amount()

products = driver.find_elements(By.CLASS_NAME, 'product-card-portrait_root__ZiRpZ')

while(current_amount <= 75):
    more_button = driver.find_element(By.CLASS_NAME, 'button-default_primary__mURfJ')
    more_button.click()
    print('......loading products')
    driver.implicitly_wait(2)

    current_amount, total_amount = get_displayed_amount()
    print(current_amount)
    
    # get new loaded products
    product_lane = driver.find_elements(By.CLASS_NAME, 'product-grid-lane_root__rii9N')[-2]
    new_products = product_lane.find_elements(By.CLASS_NAME, 'product-card-portrait_root__ZiRpZ')
    # get information about each product
    convert_product(new_products[1])

print(product_list)
