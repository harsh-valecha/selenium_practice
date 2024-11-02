import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_make_my_trip():
    driver = Chrome()
    driver.get('https://www.makemytrip.com/')
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,
                                         '//span[@data-cy="closeModal"]'))
    )
    close = driver.find_element(By.XPATH,'//span[@data-cy="closeModal"]')
    close.click()

    WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((
            ((By.CSS_SELECTOR,"input[id='fromCity']"))
        ))
    )

    from_city = driver.find_element(By.ID,"fromCity")
    # from_city.send_keys('DEL')
    actions = ActionChains(driver=driver)
    (actions.move_to_element(to_element=from_city)
      .click()
     .send_keys('del')
     .perform())

    time.sleep(3)

    driver.close()
