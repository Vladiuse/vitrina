from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_URL = 'http://127.0.0.1:8000/'
SERVER_URL = 'https://vitrina.vim-store.ru/'

URL = SERVER_URL


browser = webdriver.Chrome()
browser.get(URL)
cards = browser.find_elements(By.CLASS_NAME, 'catalog__card')
links = []
for c in cards:
    a = c.find_element(By.CSS_SELECTOR, 'a')
    link_on_product = a.get_attribute('href')
    links.append(link_on_product)
# print(links)

for link in links:
    browser.get(link)
    product_name = browser.find_element(By.CSS_SELECTOR, 'h2.booking__column-title').text
    form = browser.find_element(By.CSS_SELECTOR, 'form.form__contact')
    name_input = form.find_element(By.NAME, 'name')
    name_input.send_keys('test ' + product_name)
    time.sleep(1)
    phone_input = form.find_element(By.NAME, 'phone')
    phone_input.send_keys('+12345678')
    time.sleep(1)
    button = form.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    time.sleep(3)
    # exit()
browser.get(f'{URL}leads')

