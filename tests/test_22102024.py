'''
CSS Selector functions
1. first-child
2. last-child
3. nth-child
4. title*= 'Flip' // title contains  Flip
5. title^='Flip' //title starts wuth Flip
6. title$='kart'// title ends with kart
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_ebay_search():
    driver = webdriver.Chrome()
    driver.get('https://www.ebay.com/')
    search_box = driver.find_element(By.CSS_SELECTOR,'#gh-ac')
    search_box.send_keys('mac mini')
    search_box.send_keys(Keys.ENTER)

    list_of_items = driver.find_elements(By.CSS_SELECTOR,"span[role='heading']")
    for i in list_of_items:
        print(i.text)

    time.sleep(2)
    driver.quit()