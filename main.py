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
# opens google
driver.get('https://www.google.com/')
# helps with checking the browser page first to see that the elements required are present before
# running the program. if the element cant be found in 5 seconds then the program will time out and the window will close.
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)
# enters the Google search bar by finding the class from the code inspection
input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
# this will clear anything on the search field
input_element.clear()
# enters the text and searches
input_element.send_keys('Youtube' + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'youtube'))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'youtube')
link.click()
# keeps the browser open for 60 seconds so that I can see what's happening
time.sleep(60)
# closes the browser
driver.quit()
