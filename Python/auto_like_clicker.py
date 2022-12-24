from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def like_click():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://padlet.com/sabanokov_as/jbflph5bwjvhhihf")
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id=\"wish-2427950736\"]/div/article/div[1]/section/div/button')))
    element.click()
    driver.close()

while True:
        like_click()
        like_click()
        like_click()
        like_click()
        like_click()