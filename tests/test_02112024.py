import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_jsexecutor():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get('https://app.vwo.com')
    driver.execute_script("alert(1)")
    time.sleep(5)
    driver.quit()


def test_jswindowscroll():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get('https://selectorshub.com/xpath-practice-page/')
    driver.execute_script("window.scrollBy(0,500); ") # scrolling in y axis by 500 px
    time.sleep(5)
    driver.quit()

def test_jsgettitle():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get('https://selectorshub.com/xpath-practice-page/')
    title = driver.execute_script('return document.title')
    url = driver.execute_script('return document.URL')
    print(title,url)
    # time.sleep(5)
    driver.quit()

def test_js_scroll_into_view():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get('https://selectorshub.com/xpath-practice-page/')
    username_div = driver.find_element(By.CSS_SELECTOR,"div[id='userName']")
    driver.execute_script('arguments[0].scrollIntoView(true);',username_div)
    time.sleep(2)
    driver.quit()

def test_shadowdom():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get('https://selectorshub.com/xpath-practice-page/')
    username_div = driver.find_element(By.CSS_SELECTOR, "div[id='userName']")
    driver.execute_script('arguments[0].scrollIntoView(true);', username_div)
    time.sleep(10)
    input_box = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys('farmhouse')

    driver.quit()