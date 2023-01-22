from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome("chromedriver", options= options)
with open("../categorylinks.txt") as link_file:
    links = link_file.readlines()

for i in range(len(links)):
    url = links[i].replace("\n", "")
    category_name = url.replace("https://www.fairprice.com.sg/category/", "")
    print(category_name)
    driver.get(url)

    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    remove = ["International Selections", "Chinese New Year", "Baby, Child Toys","Bakery","Beauty Personal Care","Dairy, Chilled Eggs","Drinks","Beer, Wine Spirits","Food Cupboard","Frozen","Fruits Vegetables","Health Wellness","Housebrand","Household","Meat Seafood","Pet Supplies","Rice, Noodles Cooking Ingredients","Snacks Confectionery","Electrical Lifestyle","Relevancy"]

    product_name = ""
    products = driver.find_elements(By. CLASS_NAME, 'sc-1bsd7ul-1.eJoyLL')
    for product in products:
        check = product.get_attribute("innerHTML").replace(" &amp;", "")
        if (check not in remove) and ("span" not in check):
            if product_name != "":
                product_name += "\n"
            product_name += check

    while True:
        if "\n\n" in product_name:
            product_name = product_name.replace("\n\n", "\n")
        else:
            break

    with open(f"{category_name}.txt", "w") as link_file:
        link_file.write(product_name)