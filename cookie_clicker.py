# I have installed the selenium package on this specific program. the chromedriver is also part of the project files
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# this import is for identifying various elements on the browser automatically
from selenium.webdriver.common.by import By
# this import lets me use the keys to interact with the browser elements
from selenium.webdriver.common.keys import Keys
# these imports will help with checking the browser page first to see that the elements required are present before
# running the program
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# this accesses the chromedriver.exe file
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
# opens the website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# this code deals with the language selector
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"English")]'))
)

language = driver.find_element(By.XPATH, '//*[contains(text(),"English")]')
language.click()

cookie_id = 'bigCookie'
cookies_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = 'product'

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
# cookie.click()

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(' ')[0]
    cookies_count = int(cookies_count.replace(',', ''))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(',', '')

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
time.sleep(30)