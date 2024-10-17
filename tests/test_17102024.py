from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
driver.get() - navigate to url
driver.title - fetches title 
driver.page_source
browser options
    -
'''

def test_task2():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    page_source = driver.page_source
    assert 'google' in page_source
    driver.quit()


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options)
    driver.get('https://www.google.com/')
    driver.quit()


