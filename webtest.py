# UI-0101 ---------------------------------------------
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.get('www.....')
wd.implicitly_wait(5)

username = wd.find_elements_by_id('username')
username.send_keys('huhu')
password = wd.find_elements_by_id("password")
password.send_keys('777777777')

botton = wd.find_element_by_id('botton')
botton.click()
sidelist = wd.find_element_by_tag_name('sidelist')

for sidelist1 in sidelist:
    print(sidelist1.text)

# ------------------------------------------------------

# UI-0103 -------------------------------------------------


wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.implicitly_wait(5)

username = wd.find_elements_by_id('username')
username.send_keys("huhu")
password = wd.find_elements_by_id("password")
username.send_keys('77777777')
# 登录
client = wd.find_elements_by_class_name('client')
client.click()

modify
