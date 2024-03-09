import requests
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/hyundai_kor/")
time.sleep(3)

soup = bs(driver.page_source, 'html.parser')

article_element = soup.find('article', attrs = {
    'class' : 'x1iyjqo2'
})

a_list = article_element.find_all('a', attrs={
    'class' : '_a6hd'
}, limit=3)

data_list = []

for a in a_list:
    links = a['href']
    url = "https://www.instagram.com" + links
    driver.get(url)
    time.sleep(10)
    soup2 = bs(driver.page_source, 'html.parser')
    data = soup2.find('h1').get_text()
    # content, tag = data.split("#", maxsplit=1)
    # tag = tag.replace('#', "")
    data_list.append([data])

driver.quit()

df = pd.DataFrame(data_list)

df.to_csv('insta.csv')


